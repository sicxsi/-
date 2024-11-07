
# name: 杜比
# Author: sicxs
# Date: 2024-11-04
# export hddolby="cookie" &,@分割
# cron: 10 8 * * *
# new Env('杜比');
import requests
import re
import os,sys


def index(cookie):
     url = 'https://www.hddolby.com/index.php'
     header = {
        "authority": "www.hddolby.com",
        "method": "GET",
        "path": "/index.php",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
        "content-type": "text/html; charset=utf-8; Cache-control:private",
        "host":"www.hddolby.com",
        "referer":"https://www.hddolby.com/index.php",
        "cookie":cookie
    }
     try:
        response = requests.get(url=url,headers=header)
        info = response.text
      
        if "首页" in info:
         print("登陆成功")
        
         attendance(cookie)  
        else:
         print("登录失败")
     except Exception as e:
          print(e)
def attendance(cookie):
     url = 'https://www.hddolby.com/attendance.php'
     header = {
        "authority": "www.hddolby.com",
        "method": "GET",
        "path": "/attendance.php",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
        "content-type": "text/html; charset=utf-8; Cache-control:private",
        "host":"www.hddolby.com",
        "referer":"https://www.hddolby.com/index.php",
        "cookie":cookie
    }
     try:
        response = requests.get(url=url,headers=header)
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
     url = 'https://www.hddolby.com/torrents.php'
     header = {
        "authority": "www.hddolby.com",
        "method": "GET",
        "path": "/torrents.php",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
        "content-type": "text/html; charset=utf-8; Cache-control:private",
        "host":"www.hddolby.com",
        "referer":"https://www.hddolby.com/attendance.php",
        "cookie":cookie
    }
     try:
       response = requests.get(url=url,headers=header)
       pattern = re.compile(r"class='UltimateUser_Name'><b>(.+?)</b>")
       pattern2 = re.compile(r']: (.*)&nbsp;\(')
       pattern3 = re.compile(r'签到已得(.*?)\) ')
       

       matches = pattern.findall(response.text)
       matches1 = pattern2.findall(response.text)
       matches2 = pattern3.findall(response.text)
       


       
       print( "用户名：" + matches[0] + " 鲸币：" + matches1[0] + " 签到已得：" + matches2[0])

     except Exception as e:
         print(e)

def sicxs():
    if os.environ.get("hddolby"):
        ck = os.environ.get("hddolby")
    else:
        ck = ""
        if ck == "":
            print("请设置变量")

            sys.exit()

    ck_run = re.split(r'&|@|\n',ck)

    for i, ck_run_n in enumerate(ck_run):
        print(f'\n----------- 账号【{i + 1}/{len(ck_run)}】执行 -----------')
        try:
            
            index(ck_run_n)
        except Exception as e:
            print(e)

    print(f'\n-----------  执 行  结 束 -----------')
 
if __name__ == '__main__':
  
  sicxs()    