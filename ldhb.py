# name: 绿袋环保
# Author: sicxs
# Date: 2024-11-6
# 微信小程序
# export wx_ldhb="token"
# 多号 @,&分割 
# 建议更改昵称
# cron: 10 8 * * *
# new Env('绿袋环保');
import requests
import os,json,sys
import time,re


def GetMyInfo(token): #登录信息
    url = "https://www.lvdhb.com/MiniProgramApiCore/api/v3/My/GetMyInfo"
    header = {
            "authority": "www.lvdhb.com",
            "method": "GET",
            "path": "/MiniProgramApiCore/api/v3/My/GetMyInfo",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090c11)XWEB/11437",
            "token": token,
            "content-type": "application/json",
            "referer": "https://servicewechat.com/wx55da7d089eab6cdb/121/page-frame.html",
            }
    try:
       response = requests.get(url=url,headers=header)
       response.encoding = "utf-8"
       info = json.loads(response.text)
       if  info['signed']:
            print(f"用户名：{info['NickName']}")
            Sign(token)
            if 250 <= info['score']:
                time.sleep(3)
                SaveCash(token)
            else:
                print("积分不足，暂不提现")    
       else:
            print("获取用户信息失败")
            print(info)
       
    except Exception as e:
          
          print("你的账号可能到期了")  
def Sign(token): #签到
    url = "https://www.lvdhb.com/MiniProgramApiCore/api/v3/Login/Sign"
    header = {
        "authority": "www.lvdhb.com",
        "method": "POST",
        "path": "/MiniProgramApiCore/api/v3/Login/Sign",
        "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090a13) XWEB/8555",
        "token": token,
        "content-type": "application/json",
        "referer": "https://servicewechat.com/wx55da7d089eab6cdb/121/page-frame.html",

        }
    response = requests.post(url=url,headers=header)
    response.encoding = "utf-8"
    info = json.loads(response.text)
    try:
       if info['Success']:
            print(f"签到成功，获得：{info['Data']}积分")

       else:
           print(f"签到失败，你可能已经签到过了。")

    except Exception as e:
          
          print("你的账号可能到期了")  
def SaveCash(token):#提现
    url = "https://www.lvdhb.com/MiniProgramApiCore/api/v3/cash/SaveCash"
    header = {
        "authority": "www.lvdhb.com",
        "method": "POST",
        "path": "/MiniProgramApiCore/api/v3/cash/SaveCash",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090c11)XWEB/11437",
        "token": token,
        "content-type": "application/json",
        "referer": "https://servicewechat.com/wx55da7d089eab6cdb/121/page-frame.html",
        }
    data = {
        "AliAccount": "直接到微信钱包的余额",
        "Score": "250"
    }
    try:
       response = requests.post(url=url,headers=header,json=data)
       response.encoding = "utf-8"
       info = json.loads(response.text)
       if  info['Success']:
            print("提现成功")

       else:
            print(f"提现失败,{info['Message']}")
    except Exception as e:
          
          print("你的账号可能到期了") 
def sicxs():
    if os.environ.get("wx_ldhb"):
        ck = os.environ.get("wx_ldhb")
    else:
        ck = ""
        if ck == "":
            print("请设置变量")

            sys.exit()

    ck_run = re.split(r'&|@|\n',ck)

    for i, ck_run_n in enumerate(ck_run):
        print(f'\n----------- 账号【{i + 1}/{len(ck_run)}】执行 -----------')
        try:
            
            GetMyInfo(ck_run_n)
        except Exception as e:
            print(e)

    print(f'\n-----------  执 行  结 束 -----------')
if __name__ == '__main__':
       
 sicxs()