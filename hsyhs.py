
# name: 回收猿回收
# Author: sicxs
# Date: 2024-11-8
# 微信小程序
# export wx_hsyhs="auth#username" 
# 抓小程序 -> 我的 auth和username值
# 多号 @,&分割 
# cron: 16 8 * * *

import requests
import json,os,sys,re
import hashlib

# md5 = "action=user&appkey=1079fb245839e765&merchant_id=2&method=center&username={wx_username}UppwYkfBlk"
# md5_hash = hashlib.md5(md5.encode('utf-8')).hexdigest().upper().lower()
# print(md5_hash) 
# sign为固定值 

def index(wx_auth,wx_username): #登录信息
   url = f"https://www.52bjy.com/api/app/user.php?action=userinfo&app=hsywx&appkey=1079fb245839e765&auth={wx_auth}&merchant_id=2&username={wx_username}"
   header = {
        "authority": "www.52bjy.com",
        "method": "GET",
        "path": "/api/app/user.php?action=userinfo&app=hsywx&appkey=1079fb245839e765&auth={wx_auth}&merchant_id=2&username={wx_username}",
        "scheme": "https",
        "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090a13) XWEB/8555",
        "content-type": "application/json",
        "referer": "https://servicewechat.com/wxadd84841bd31a665/91/page-frame.html"
        }
   response = requests.get(url=url,headers=header)
   response.encoding = "utf-8"
   info = json.loads(response.text)
   if info['isSucess']:
       print(f"登陆成功，用户名：{info['data']['nickname']}")
       md5 = f"action=user&app=hsywx&appkey=1079fb245839e765&merchant_id=2&method=qiandao&username={wx_username}&version=2UppwYkfBlk"
       wx_sign = hashlib.md5(md5.encode('utf-8')).hexdigest().upper().lower()
       qiandao(wx_username,wx_sign)
   else:
       print(info['message'])    

def qiandao(wx_username,wx_sign): #签到
    url = f"https://www.52bjy.com/api/app/hsy.php?action=user&app=hsywx&appkey=1079fb245839e765&merchant_id=2&method=qiandao&username={wx_username}&version=2&sign={wx_sign}"
    header = {
            "authority": "www.52bjy.com",
            "method": "POST",
            "path": f"/api/app/hsy.php?action=user&app=hsywx&appkey=1079fb245839e765&merchant_id=2&method=qiandao&username={wx_username}&version=2",
            "scheme": "https",
            "envconnection": "test",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090c11)XWEB/11437",
            "content-type": "application/json",
            "referer": "https://servicewechat.com/wxadd84841bd31a665/91/page-frame.html",
            }
    response = requests.post(url=url,headers=header)
    response.encoding = "utf-8"
    info = json.loads(response.text)
    md5 = f"action=user&appkey=1079fb245839e765&merchant_id=2&method=center&username={wx_username}UppwYkfBlk"
    wx_sign_info = hashlib.md5(md5.encode('utf-8')).hexdigest().upper().lower()
    if info['isSucess']:
       print(info['message'])
       print(f"签到红包：{info['data']['qiandao_award']}元，签到天数：{info['data']['double_award_days']}")
       info(wx_username,wx_sign_info)
    else:
       print(info['message']) 
       signinfo(wx_username,wx_sign_info)
def signinfo(wx_username,wx_sign_info): #红包
    url = f"https://www.52bjy.com/api/app/hsy.php?action=user&appkey=1079fb245839e765&merchant_id=2&method=center&username={wx_username}&sign={wx_sign_info}"
    header = {
        "authority": "www.52bjy.com",
        "method": "GET",
        "path": f"/api/app/hsy.php?action=user&appkey=1079fb245839e765&merchant_id=2&method=center&username={wx_username}&sign={wx_sign_info}",
        "scheme": "https",
        "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090a13) XWEB/8555",
        "content-type": "application/json",
        "referer": "https://servicewechat.com/wxadd84841bd31a665/91/page-frame.html"
        }
    response = requests.get(url=url,headers=header)
    response.encoding = "utf-8"
    info = json.loads(response.text)
    if info['isSucess']:
       print(f"红包总额：{info['data']['yuanbao']}元") 
    else:
        print(info)  

def sicxs():
    cookie = os.environ.get("wx_hsyhs", "")
    if not cookie:
        print("请设置变量export wx_hsyhs")
        sys.exit()
    s_cookie = re.split(r'@|&|\n', cookie)
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
