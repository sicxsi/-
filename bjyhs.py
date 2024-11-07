
# name: 白鲸鱼回收
# Author: sicxs
# Date: 2024-11-6
# 微信小程序
# export wx_bjyhs="auth#username" 
# 抓小程序auth和username值
# 多号 @,&分割 
# cron: 25 8 * * *
# new Env('白鲸鱼回收');
import requests
import os,json,sys
import time,re

def userinfo(s_auth,s_username): #登录信息
    url = f"https://www.52bjy.com/api/app/user.php?action=userinfo&auth={s_auth}&username={s_username}"
    header = {
        "authority": "www.52bjy.com",
        "method": "GET",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090c11)XWEB/11437",
        "content-type": "application/json",
        "referer": "https://servicewechat.com/wxc525caf8e3a9e434/305/page-frame.html",
        }
    data = {
        "action": "userinfo",
        "auth": s_auth,
        "username": s_username,
        }
    response = requests.get(url=url,headers=header,data=data)
    response.encoding = "utf-8"
    info = json.loads(response.text)
    try:
       if  info['isSucess']:
            print(f"用户名：{info['data']['truename']}")
            time.sleep(3)
            qiandao(s_auth,s_username)
       else:
            print("获取用户信息失败")
            print(info)
    except Exception as e:
          
          print("你的账号可能到期了")  
def qiandao(s_auth,s_username): #签到
    url = f"https://www.52bjy.com/api/app/user.php?action=qiandao&auth={s_auth}&username={s_username}"
    header = {
        "authority": "www.52bjy.com",
        "method": "GET",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090c11)XWEB/11437",
        "content-type": "application/json",
        "referer": "https://servicewechat.com/wxc525caf8e3a9e434/305/page-frame.html",
        }
    data = {
        "action": "userinfo",
        "auth": s_auth,
        "username": s_username,
        }
    response = requests.get(url=url,headers=header,data=data)
    response.encoding = "utf-8"
    info = json.loads(response.text)
    try:
       if  info['isSucess']:
            print(f"签到成功")
       else:
            print(info['message'])
    except Exception as e:
          
          print("你的账号可能到期了")  

def sicxs():
    if os.environ.get("wx_bjyhs"):
        ck = os.environ.get("wx_bjyhs")
    else:
        ck = ""
        if ck == "":
            print("请设置变量")

            sys.exit()

    ck_run = re.split(r'&|@|\n',ck)

    for i, ck_run_n in enumerate(ck_run):
        print(f'\n----------- 账号【{i + 1}/{len(ck_run)}】执行 -----------')
        params_list = ck_run_n.split('#')
        try:  
            userinfo(params_list[0],params_list[1])
        except Exception as e:
            print(e)

    print(f'\n-----------  执 行  结 束 -----------')
if __name__ == '__main__':
       
 sicxs()  
