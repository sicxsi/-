
# name: ikun vpn
# Author: sicxs
# Date: 2024-11-5
# export ikun="cookie" @,&分割 
# cron: 0 8 * * *
# new Env('ikun vpn');
import requests
import os,sys,time,re
import json,re

def info(cookie): #登录信息
    url = "https://ikuuu.one/user"
    header ={
        "authority": "ikuuu.one",
        "method": "GET",
        "path": "/user",
        "scheme": "https",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "referer": "https://ikuuu.one/auth/login",
        "cookie": cookie,
        }
    try:
        response = requests.get(url=url,headers=header)
        info = response.text
        pattern = re.compile(r'div class="(.*?)">(.*?)</div>')
        matches = pattern.findall(info)
        print(f"登陆成功，{matches[1][1]}")
        time.sleep(3)
        qiandao(cookie)
    except Exception as e:
          print(e)   

def user(cookie): #流量
    url = "https://ikuuu.one/user"
    header ={
        "authority": "ikuuu.one",
        "method": "GET",
        "path": "/user",
        "scheme": "https",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "referer": "https://ikuuu.one/auth/login",
        "cookie": cookie,
        }
    try:
        response = requests.get(url=url,headers=header)
        info = response.text
        pattern1 = re.compile(r'<span class="(.*?)">(.*?)</span> (...?)')
        matches1 = pattern1.findall(info)
        print(f"总流量：{matches1[0][1]}{matches1[0][2]}")
       
    except Exception as e:
          print(e)
def  qiandao(cookie): #签到

    url = "https://ikuuu.one/user/checkin"
    header ={
        "authority": "ikuuu.one",
        "method": "GET",
        "path": "/user/checkin",
        "scheme": "https",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "referer": "https://ikuuu.one/auth/login",
        "cookie": cookie,
        }
    try:
        response = requests.post(url=url,headers=header)
        response.encoding = "utf-8"
        info = json.loads(response.text)
        if 1== info['ret']:
         print(f"恭喜,{info['msg']}")
         user(cookie)
        else:
         print("请勿重复签到")  
         user(cookie)
    except Exception as e:
        print(e)
def sicxs():
    if os.environ.get("ikun"):
        ck = os.environ.get("ikun")
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