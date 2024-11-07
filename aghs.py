# name: 爱裹回收
# Author: sicxs
# Date: 2024-11-5
# 微信小程序
# export wx_aghs="uid" @,&分割 
# cron: 15 8 * * *
# new Env('爱裹回收');

import requests
import os,sys,time
import json,re
 
def qiandao1(Authorization): #签到状态
    url = "https://alipay.haliaeetus.cn/fuli/api/fuli/signedInfo"
    header = {
            "Host": "alipay.haliaeetus.cn",
            "Connection": "keep-alive",
            "plateForm": "WX",
            "xweb_xhr": "1",
            "Authorization":Authorization,
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090c11)XWEB/11437",
            "channelNo": "",
            "Content-Type": "application/json",
            "Accept": "*/*",
            "Sec-Fetch-Site": "cross-site",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "https://servicewechat.com/wx4ff260333d3c5ddd/211/page-frame.html",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9"
            }
    try:
        response = requests.get(url=url,headers=header)
        info = json.loads(response.text)
        if 200 == info['status']:
            print(f"您已签到,{info['data']['signDays']}天")
        else:
            print("查询失败")   

    except Exception as e:
          
          print("你的账号可能到期了")    

def qiandao(Authorization): #签到
    url ="https://alipay.haliaeetus.cn/fuli/api/fuli/signed"
    header = {
        "Host": "alipay.haliaeetus.cn",
        "Connection": "keep-alive",
        "plateForm": "WX",
        "xweb_xhr": "1",
        "Authorization":Authorization,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090c11)XWEB/11437",
        "channelNo": "",
        "Content-Type": "application/json",
        "Accept": "*/*",
        "Sec-Fetch-Site": "cross-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://servicewechat.com/wx4ff260333d3c5ddd/211/page-frame.html",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9"
        }
    try:
        response = requests.get(url=url,headers=header)
        info = json.loads(response.text)
        if 200 == info['status']:
            print("签到成功")
            time.sleep(3)
            qiandao1(Authorization)
        elif 500 == info['status']:
            print("您今日已签到！")
            time.sleep(3)
            qiandao1(Authorization)
        else:
            print("签到失败")   
    except Exception as e:
          
          print("你的账号可能到期了")    
def info(Authorization):#我的信息
    url ="https://alipay.haliaeetus.cn/recy/api/auth/asset/getInfo"
    header = {
        "Host": "alipay.haliaeetus.cn",
        "Connection": "keep-alive",
        "plateForm": "WX",
        "xweb_xhr": "1",
        "Authorization":Authorization,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090c11)XWEB/11437",
        "channelNo": "",
        "Content-Type": "application/json",
        "Accept": "*/*",
        "Sec-Fetch-Site": "cross-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://servicewechat.com/wx4ff260333d3c5ddd/211/page-frame.html",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9"
        }
    try:
        response = requests.post(url=url,headers=header)
        info = json.loads(response.text)
        if 200 == info['status']:
          print(f"用户名：{info['data']['userName']}")
          time.sleep(3)
          qiandao(Authorization)
        else:
            print("失败")
    except Exception as e:
          
          print("你的账号可能到期了")    
     
def sicxs():
    if os.environ.get("wx_aghs"):
        ck = os.environ.get("wx_aghs")
    else:
        ck = ""
        if ck == "":
            print("请设置变量")

            sys.exit()

    ck_run = re.split(r'&|@|\n',ck)

    for i, ck_run_n in enumerate(ck_run):
        print(f'\n----------- 账号【{i + 1}/{len(ck_run)}】执行 -----------')
        try:
            
            info(ck_run_n)
        except Exception as e:
            print(e)

    print(f'\n-----------  执 行  结 束 -----------')
if __name__ == '__main__':
       
 sicxs()


