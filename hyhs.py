"""
name: 好衣回收
Author: sicxs
Date: 2024-11-5
微信小程序
export wx_hyhs="uid" @,&分割 
cron: 0 8 * * *
"""
import requests
import os,sys,time
import json
uid = "122044"

def index(uid):#登录
    url = "https://haoyi.haojim.com/index/user/getInfo"
    header = {
        "authority": "haoyi.haojim.com",
        "method": "POST",
        "path": "/index/user/getInfo",
        "scheme": "https",
        "content-length": "14",
        "xweb_xhr": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090c11)XWEB/11437",
        "content-type": "application/json",
        "accept": "*/*",
        "sec-fetch-site": "cross-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://servicewechat.com/wxeb7817d0f294caf1/11/page-frame.html",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9"
        }
    data ={        
     "uid":uid
        }
    try:
        response = requests.post(url=url,json=data,headers=header)
        response.encoding = "utf-8"
        info = json.loads(response.text)
        if 0 == info['errno']:
             print("登陆成功")
             time.sleep(2)
             qiandao(uid)
        else:
             print("登陆失败,请稍后再试")                
    except Exception as e:
          print("你输入的UID可能有问题")
def qiandao(uid):#签到
      url = "https://haoyi.haojim.com/index/user/qiandao"
      header = {
        "authority": "haoyi.haojim.com",
        "method": "POST",
        "path": "/index/user/qiandao",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090c11)XWEB/11437",
        "content-type": "application/json",
        "referer": "https://servicewechat.com/wxeb7817d0f294caf1/11/page-frame.html",
        }
      data ={        
        "uid":uid,
        "isqd":0
        }
      try:  
        response = requests.post(url=url,json=data,headers=header)
        response.encoding = "utf-8"
        info = json.loads(response.text)
        if 0 == info['errno']:
            print("签到成功")

            qiandaoinfo(uid)
        else:
            print("签到失败")               
      except Exception as e:
            print("你输入的UID可能有问题")
def qiandaoinfo(uid):#我的信息
      url = "https://haoyi.haojim.com/index/user/qiandaoinfo"
      header = {
        "authority": "haoyi.haojim.com",
        "method": "POST",
        "path": "/index/user/qiandaoinfo",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090c11)XWEB/11437",
        "content-type": "application/json",
        "referer": "https://servicewechat.com/wxeb7817d0f294caf1/11/page-frame.html",
        }
      data ={        
        "uid":uid
        }
      try:  
        response = requests.post(url=url,json=data,headers=header)
        response.encoding = "utf-8"
        info = json.loads(response.text)
        if 0 == info['errno']:
            print(f"用户名：{info['data']['nickname']},获取奖励：{info['data']['money']}，签到天数：{info['data']['qd_days']}")
        else:
            print("签到失败")               
      except Exception as e:
            print("你输入的UID可能有问题")
            
def sicxs():
    if os.environ.get("wx_hyhs"):
        ck = os.environ.get("wx_hyhs")
    else:
        ck = ""
        if ck == "":
            print("请设置变量")

            sys.exit()

    ck_run = ck.split('@|&')

    for i, ck_run_n in enumerate(ck_run):
        print(f'\n----------- 账号【{i + 1}/{len(ck_run)}】执行 -----------')
        try:
            
            index(ck_run_n)
        except Exception as e:
            print(e)

    print(f'\n-----------  执 行  结 束 -----------')
if __name__ == '__main__':
       
 sicxs()