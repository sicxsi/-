"""
name: 家园
Author: sicxs
Date: 2024-10-29
export hdhome="cookie" &,@分割
cron: 0 5 * * *
"""
import requests
import re
import os,sys

s = requests.session()
def index(cookie):
     url = 'https://hdhome.org/index.php'
     header = {
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
        "content-type": "text/html; charset=utf-8; Cache-control:private",
        "host":"hdhome.org",
        "referer":"https://hdhome.org/torrents.php",
        "cookie":cookie
    }
     try:
        response = s.get(url=url,headers=header)
        info = response.text
        if "首页" in info:
         print("登陆成功")
        
         attendance(cookie)  
        else:
         print("登录失败")
     except Exception as e:
          print(e)
def attendance(cookie):
     url = 'https://hdhome.org/attendance.php'
     header = {
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
        "content-type": "text/html; charset=utf-8; Cache-control:private",
        "host":"hdhome.org",
        "referer":"https://hdhome.org/torrents.php",
        "cookie":cookie
    }
     try:
        response = s.get(url=url,headers=header)
        info = response.text
        if "签到成功" in info:
           
           print("签到成功")

           torrents(cookie)

        elif "您今天已经签到过了" in info:
         
         print("您今天已经签到过了，请勿重复刷新。")

         torrents(cookie)

        else :
          print("签到失败")

     except Exception as e:
          print(e)
def torrents(cookie):
     url = 'https://hdhome.org/torrents.php'
     header = {
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
        "content-type": "text/html; charset=utf-8; Cache-control:private",
        "host":"hdhome.org",
        "referer":"https://hdhome.org",
        "cookie":cookie
    }
     try:
       response = s.get(url=url,headers=header)
       pattern = re.compile(r"class='CrazyUser_Name'><b>(.+?)</b>")
       pattern2 = re.compile(r']: (.*)&nbsp;\(')
       pattern3 = re.compile(r'签到已得(.*?)\) ')
       pattern4 = re.compile(r'做种积分：</font>(.*?) ')
    

       matches = pattern.findall(response.text)
       matches1 = pattern2.findall(response.text)
       matches2 = pattern3.findall(response.text)
       matches3 = pattern4.findall(response.text)
       
       
       print( "用户名：" + matches[0] + " 魔力值：" + matches1[0] + " 签到已得：" + matches2[0]+ " 做种积分：" + matches3[0])

     except Exception as e:
         print(e)

def sicxs():
    if os.environ.get("hdhome"):
        ck = os.environ.get("hdhome")
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
 