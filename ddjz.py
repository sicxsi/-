# name: 点点兼职
# Author: sicxs
# Date: 2024-11-7
# 微信小程序
# export wx_ddjz="api_auth_code#api_auth_uid"  多账户@,&分割 
#微信抓api_auth_code和api_auth_uid的注意不要写反
#提现需要实名认证
# cron: 15 8 * * *
# new Env('点点兼职');

import requests
import os,sys,time
import json,re

def index(api_auth_code,api_auth_uid):#登录信息
    
    url= f"https://mili.shensemiao.com/index.php?v=1&appid=4&appsecret=PHPCMF19F5DF41B263B&api_auth_code={api_auth_code}&api_auth_uid={api_auth_uid}&s=yhxcx&c=home&m=member_index"
    header = {
          "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090a13) XWEB/8555",
          "Content-Type": "application/x-www-form-urlencoded",
          "referer": "https://servicewechat.com/wxec97c88d99c5d385/5/page-frame.html",
        }
    response = requests.post(url=url,headers=header)
    response.encoding = "utf-8"
    info = json.loads(response.text)
    if 1 ==info['code']:
        print(f"用户名：{info['data']['member']['name']}")
        time.sleep(3)
        qiandaoinfo(api_auth_code,api_auth_uid)
        time.sleep(16)
        qiandao(api_auth_code,api_auth_uid)
        time.sleep(16)
        qiandao1(api_auth_code,api_auth_uid)
        time.sleep(16)
        qiandao2(api_auth_code,api_auth_uid)
    else:
        print("登录失败")   

def qiandao(api_auth_code,api_auth_uid):#签到
    url = f"https://mili.shensemiao.com/index.php?v=1&appid=4&appsecret=PHPCMF19F5DF41B263B&api_auth_code={api_auth_code}&api_auth_uid={api_auth_uid}&s=member&app=Yhxcx&c=qd&m=sign_in"
    header = {
          "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090a13) XWEB/8555",
          "Content-Type": "application/x-www-form-urlencoded",
          "referer": "https://servicewechat.com/wxec97c88d99c5d385/5/page-frame.html",
        }

    data={
            "id": "1893",
            "fblx": "1",
            "wcs": "0",
            "theway": "signin",
            "search": "1"
          }
    
    response = requests.post(url=url,headers=header,data=data)
    response.encoding = "utf-8"
    info = json.loads(response.text)
    if 1 ==info['code']:
        print("看视频成功，看下一个")
    elif 0 ==info['code']:
        print("你已经签到过了，请勿重复签到。")  
        sys.exit() 
    else:
        print("失败")   

def qiandao1(api_auth_code,api_auth_uid):#签到1
    url = f"https://mili.shensemiao.com/index.php?v=1&appid=4&appsecret=PHPCMF19F5DF41B263B&api_auth_code={api_auth_code}&api_auth_uid={api_auth_uid}&s=member&app=Yhxcx&c=qd&m=sign_in"
    header = {
          "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090a13) XWEB/8555",
          "Content-Type": "application/x-www-form-urlencoded",
          "referer": "https://servicewechat.com/wxec97c88d99c5d385/5/page-frame.html",
        }

    data={
            "id": "2203",
            "fblx": "1",
            "wcs": "1",
            "theway": "signin",
            "search": "1"
          }
    
    response = requests.post(url=url,headers=header,data=data)
    response.encoding = "utf-8"
    info = json.loads(response.text)
    if 1 ==info['code']:
        print("看视频成功，查询是否签到成功")
    elif 0 ==info['code']:
        print("你已经签到过了，请勿重复签到。")
        sys.exit()       
    else:
        print("失败")   

def qiandao2(api_auth_code,api_auth_uid):#签到成功判断
    
    url = f"https://mili.shensemiao.com/index.php?v=1&appid=4&appsecret=PHPCMF19F5DF41B263B&api_auth_code={api_auth_code}&api_auth_uid={api_auth_uid}&s=member&app=Yhxcx&c=qd&m=sign_in"
    header = {
          "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090a13) XWEB/8555",
          "Content-Type": "application/x-www-form-urlencoded",
          "referer": "https://servicewechat.com/wxec97c88d99c5d385/5/page-frame.html",
        }
    data = {
          "fblx": "1",
          "wcs": "1",
          "theway": "signin",
          "search": "1"
        }
    response = requests.post(url=url,headers=header,data=data)
    response.encoding = "utf-8"
    info = json.loads(response.text)
    if 0 ==info['code']:
        print(info['msg'])
    else:
        print("失败")   
        print(info)

def qiandaoinfo(api_auth_code,api_auth_uid):#初始化签到
    url = f"https://mili.shensemiao.com/index.php?v=1&appid=4&appsecret=PHPCMF19F5DF41B263B&&api_auth_code={api_auth_code}&api_auth_uid={api_auth_uid}&&s=member&app=yhxcx&c=qd&m=sign_in"
    header = {
          "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090a13) XWEB/8555",
          "Content-Type": "application/x-www-form-urlencoded",
          "referer": "https://servicewechat.com/wxec97c88d99c5d385/5/page-frame.html",
        }

    response = requests.post(url=url,headers=header)
    response.encoding = "utf-8"
    info = json.loads(response.text)

    if 1 ==info['code']:
        print("正在进行签到，请稍等。")
    else:
        print(info)   
        sys.exit() 

def sicxs():
    cookie = os.environ.get("wx_ddjz", "")
    if not cookie:
        print("请设置变量 wx_ddjz")
        sys.exit()
    s_cookie = re.split(r'&|@|\n', cookie)
    for i, s_info_ck in enumerate(s_cookie):
        print(f'\n----------- 账号【{i + 1}/{len(s_cookie)}】执行 -----------')
        params_list = re.split(r'#', s_info_ck)
        if len(params_list) >= 2:
            try:
                index(params_list[0], params_list[1])
            except Exception as e:
                print(f"执行账号【{i + 1}】时发生错误: {e}")
        else:
            print(f"账号【{i + 1}】的参数不足，跳过该账号。")

    print(f'\n-----------  执 行  结 束 -----------')

if __name__ == '__main__':
       
 sicxs()