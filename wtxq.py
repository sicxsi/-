# name: 捂碳星球
# Author: sicxs
# Date: 2024-11-7
# 微信小程序
#手动先签到一次,带提现，需要测试
# export wx_wtxq="authorization" @,&分割  不需要Bearer 
# cron: 15 8 * * *
# new Env('捂碳星球');
import requests
import os,sys,time
import json,re


def inde(authorization): #登录信息
    url = "https://wt.api.5tan.com/api/user/index?platform=1"
    header = {
        "authority": "wt.api.5tan.com",
        "method": "GET",
        "path": "/api/user/index?platform=1",
        "authorization": f"Bearer {authorization}",
        "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090a13) XWEB/8555",
        "content-type": "application/json",
        "referer": "https://servicewechat.com/wx54c4768a6050a90e/217/page-frame.html",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9"
        }
    
    response = requests.get(url=url,headers=header)
    info = json.loads(response.text)
    if 200 == info['code']:
      print(f"登录成功,用户名:{info['data']['nick_name']}")
      time.sleep(2)
      qiandao(authorization)
      time.sleep(2)
      money(authorization)
    else:
        print("失败")
def qiandao(authorization): #签到
    url = "https://wt.api.5tan.com/api/signin/addSignIn"
    header = {
        "authority": "wt.api.5tan.com",
        "method": "GET",
        "path": "/api/signin/addSignIn",
        "authorization": f"Bearer {authorization}",
        "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090a13) XWEB/8555",
        "content-type": "application/json",
        "referer": "https://servicewechat.com/wx54c4768a6050a90e/217/page-frame.html",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9"
        }
    data =  {"platform":1}
    response = requests.post(url=url,headers=header,json=data)
    info = json.loads(response.text)
    if 200 == info['code']:
      print(info['data']['title'])
    elif -1 == info['code']:  
     print(info['msg'])
    else:
     print("签到失败，你的authorization可能过期了。")
def money(authorization): #红包信息

    url = "https://wt.api.5tan.com/api/user/index?platform=1"
    header = {
        "authority": "wt.api.5tan.com",
        "method": "GET",
        "path": "/api/user/index?platform=1",
        "authorization": f"Bearer {authorization}",
        "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090a13) XWEB/8555",
        "content-type": "application/json",
        "referer": "https://servicewechat.com/wx54c4768a6050a90e/217/page-frame.html",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9"
        }
    
    response = requests.get(url=url,headers=header)
    info = json.loads(response.text)
    if 200 == info['code']:
      print(f"红包总额{info['data']['money']}")
      if 1 < info['data']['money']:
         cash(authorization)
    else:
        print("失败") 
def cash(authorization): #提现
    url = "https://wt.api.5tan.com/api/logmoney/cash"
    header = {
        "authority": "wt.api.5tan.com",
        "method": "GET",
        "path": "/api/logmoney/cash",
        "authorization": f"Bearer {authorization}",
        "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090a13) XWEB/8555",
        "content-type": "application/json",
        "referer": "https://servicewechat.com/wx54c4768a6050a90e/217/page-frame.html",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9"
        }
    data =  {"money":"1","platform":1}
    response = requests.post(url=url,headers=header,json=data)
    info = json.loads(response.text)
    if 200 == info['code']:
      print(info['data'])
    elif -1 == info['code']:  
     print(info['msg'])
    else:
     print("失败。")
def sicxs():
    cookie = os.environ.get("wx_wtxq", "")
    if not cookie: 
        print("请设置变量 wx_wtxq")
        sys.exit()
    s_cookie = re.split(r'&|@|\n', cookie)
    for i, s_cookie_1 in enumerate(s_cookie):
        print(f'\n----------- 账号【{i + 1}/{len(s_cookie_1)}】执行 -----------')
        try:
            inde(s_cookie_1)
        except Exception as e:
            print(f"执行账号【{i + 1}】时发生错误: {e}")

    print(f'\n-----------  执 行  结 束 -----------')
if __name__ == '__main__':
       
 sicxs()
