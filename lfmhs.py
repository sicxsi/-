"""
name: 绿蜂蜜回收
Author: sicxs
Date: 2024-11-6
微信小程序
export wx_lmfhs="access_token#user_token" access_token#user_token分割 
多号 @,&分割 
其他时候不要再进小程序
cron: 0 8 * * *
"""
import requests
import os,sys
import json

access_token ="bf453854f863b1e7ebe140c7f52f1b75"
user_token ="520182d4a2276c95af16f4b1bf61a4cd"

def toSign(access_token,user_token):#签到

     url = "https://lmf.lvmifo.com/api/5dca57afa379e?m=toSign"

     header = {
        "Host": "lmf.lvmifo.com",
        "access-token": access_token,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090c11)XWEB/11437",
        "Content-Type": "application/x-www-form-urlencoded",
        "xweb_xhr": "1",
        "user-token": user_token,
        "lat": "",
        "this-shop-id": "0",
        "version": "v1.0.0",
        "Accept": "*/*",
        "Sec-Fetch-Site": "cross-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://servicewechat.com/wx6fcde446296d9588/240/page-frame.html",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9"
          }
     data = {
            "m": "toSign"
            }
     try:
       response = requests.get(url=url,headers=header,data=data)
       response.encoding = "utf-8"
       info = json.loads(response.text)
       if 1 == info['code']:
            print(f"签到成功，签到次数{info['data']['get_red_packet']}天，获得红包{info['data']['get_red_packet']}元")
       elif -1 == info['code']:
            print("今日已签到！")
       else:
            print("签到失败")
     except Exception as e:
          
          print("你的账号可能到期了")    
def getUserInfo(access_token,user_token):#登录信息
     
     url = "https://lmf.lvmifo.com/api/5dca57afa379e?m=getUserInfo"
     header = {
        "Host": "lmf.lvmifo.com",
        "access-token": access_token,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090c11)XWEB/11437",
        "Content-Type": "application/x-www-form-urlencoded",
        "xweb_xhr": "1",
        "user-token": user_token,
        "lat": "",
        "this-shop-id": "0",
        "version": "v1.0.0",
        "Accept": "*/*",
        "Sec-Fetch-Site": "cross-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://servicewechat.com/wx6fcde446296d9588/240/page-frame.html",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9"
          }
     data = {
            "m": "getUserInfo"
            }
     try:
       response = requests.get(url=url,headers=header,data=data)
       response.encoding = "utf-8"
       info = json.loads(response.text)
       if 1 == info['code']:
            print(f"用户名：{info['data']['nick_name']}")

            toSign(access_token,user_token)
       else:
            print("获取用户信息失败")
            print(info)
       
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

    ck_run = ck.split('@|&')

    for i, ck_run_n in enumerate(ck_run):
        print(f'\n----------- 账号【{i + 1}/{len(ck_run)}】执行 -----------')
        params_list = ck_run_n.split('#')
        try:  
            getUserInfo(params_list[0],params_list[1])
        except Exception as e:
            print(e)

    print(f'\n-----------  执 行  结 束 -----------')
if __name__ == '__main__':
       
 sicxs()  