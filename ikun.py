
# name: ikun vpn
# Author: sicxs
# Date: 2024-11-5
# export ikun="账号#密码" & 换行分割 
# cron: 0 8 * * *
# new Env('ikun vpn');
import requests
import os,sys,time,re
import json,re

def index(wy_user,wy_pass):#账号密码登录

    url = "https://ikuuu.one/auth/login"
    header = {
        "authority": "ikuuu.one",
        "method": "POST",
        "path": "/auth/login",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
        "accept": "application/json, text/javascript, */*; q=0.01",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "origin": "https://ikuuu.one",
        "referer": "https://ikuuu.one/auth/login",
    }

    data = {
        "host": "ikuuu.one",
        "email": wy_user, 
        "passwd": wy_pass,
        "code": ""
    }
    response = requests.post(url=url, headers=header, data=data)
    cookies = response.cookies
    info(cookies)

def info(cookies): #登录信息
    url = "https://ikuuu.one/user"
    header ={
        "authority": "ikuuu.one",
        "method": "GET",
        "path": "/user",
        "scheme": "https",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "referer": "https://ikuuu.one/auth/login",
        # "cookie": cookie,
        }

    response = requests.get(url=url,headers=header,cookies=cookies)
    info = response.text
    pattern = re.compile(r'div class="(.*?)">(.*?)</div>')
    matches = pattern.findall(info)
    print(f"{matches[1][1]}")
    time.sleep(3)
    qiandao(cookies)
 
def user(cookies): #流量
    url = "https://ikuuu.one/user"
    header ={
        "authority": "ikuuu.one",
        "method": "GET",
        "path": "/user",
        "scheme": "https",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "referer": "https://ikuuu.one/auth/login",
       # "cookie": cookie,
        }
    try:
        response = requests.get(url=url,headers=header,cookies=cookies)
        info = response.text
        pattern1 = re.compile(r'<span class="(.*?)">(.*?)</span> (...?)')
        matches1 = pattern1.findall(info)
        print(f"总流量：{matches1[0][1]}{matches1[0][2]}")
       
    except Exception as e:
          print(e)
def  qiandao(cookies): #签到

    url = "https://ikuuu.one/user/checkin"
    header ={
        "authority": "ikuuu.one",
        "method": "GET",
        "path": "/user/checkin",
        "scheme": "https",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "referer": "https://ikuuu.one/auth/login",
      #  "cookie": cookie,
        }
    try:
        response = requests.post(url=url,headers=header,cookies=cookies)
        response.encoding = "utf-8"
        info = json.loads(response.text)
        if 1== info['ret']:
         print(f"恭喜,{info['msg']}")
         user(cookies)
        else:
         print("请勿重复签到")  
         user(cookies)
    except Exception as e:
        print(e)
def sicxs():
    cookie = os.environ.get("ikun", "")
    if not cookie:
        print("请设置变量 ikun")
        sys.exit()
    s_cookie = re.split(r'&|\n', cookie)
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
