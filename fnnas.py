"""
name: 飞牛nas
Author: sicxs
Date: 2024-11-4
export fnnas="cookie" @,& 分割
cron: 0 5 * * *
"""

import requests
import re,os,sys

def index(cookie):
     url = 'https://club.fnnas.com'
     header = {
        "Connection": "keep-alive",
        "host": "club.fnnas.com",
        "method": "GET",
        "path": "/",
        "referer":"https://club.fnnas.com/member.php?mod=logging&action=login",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
        "content-type": "text/html; charset=utf-8; Cache-control:private",
        "cookie":cookie
    }
     try:
        response = requests.get(url=url,headers=header)
        info = response.text
        if "首页" in info:
         print("登陆成功")  
         sgin(cookie)
        else:
         print("登录失败")
     except Exception as e:
          print(e)
def sgin(cookie):
     url = 'https://club.fnnas.com/plugin.php?id=zqlj_sign&sign=efd71389'
     header = {
        "Connection": "keep-alive",
        "host": "club.fnnas.com",
        "method": "GET",
        "path": "/plugin.php?id=zqlj_sign&sign=efd71389",
        "referer":"https://club.fnnas.com/plugin.php?id=zqlj_sign",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
        "content-type": "text/html; charset=utf-8; Cache-control:private",
        "cookie":cookie
    }
     try:
        response = requests.get(url=url,headers=header)
        info = response.text
        if "您今天已经打过卡了，请勿重复操作！" in info:
         
         print("您今天已经打过卡了，请勿重复操作！")  
         my(cookie)
        elif "打卡成功"in info:
         
         
         print("打卡成功")
         my(cookie)
     except Exception as e:
          print(e)
def my(cookie):
     url = 'https://club.fnnas.com/home.php'
     header = {
        "Connection": "keep-alive",
        "host": "club.fnnas.com",
        "method": "GET",
        "path": "/home.php",
        "referer":"https://club.fnnas.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
        "content-type": "text/html; charset=utf-8; Cache-control:private",
        "cookie":cookie
    }
     try:
        response = requests.get(url=url,headers=header)
        pattern = re.compile(r"em>用户名</em>(.*?)<")
        pattern2 = re.compile(r'<em>飞牛币</em>(.*?) </li>')
        pattern3 = re.compile(r'<em>登陆天数</em>(.*?) </li>')
        pattern4 = re.compile(r'金钱<span>(.*?)</span>')
    

        matches = pattern.findall(response.text)
        matches1 = pattern2.findall(response.text)
        matches2 = pattern3.findall(response.text)
        matches3 = pattern4.findall(response.text)

        # print(matches)
        # print(matches1)
        # print(matches2)
        # print(matches3)

        print( "用户名：" + matches[0] + " 飞牛币：" + matches1[0] + " 登录天数：" + matches2[0] + " 金钱：" + matches3[0])

     except Exception as e:
         print(e)

def sicxs():
    if os.environ.get("fnnas"):
        ck = os.environ.get("fnnas")
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