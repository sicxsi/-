"""
name: 全球主机论坛
Author: sicxs
Date: 2024-11-4
export hostloc="cookie" @,&分割
cron: 0 8 * * *
"""
import requests
import re,os,sys
import time
import random

s = requests.session()

def index(cookie): #登录
     url = 'https://hostloc.com'
     header = {
        "Connection":"keep-alive",
        "authority":"hostloc.com",
        "method":"GET",
        "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "referer":"https://hostloc.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0",
        "content-type": "text/html; charset=utf-8",
        "cookie":cookie
    }
     try:
        response = s.get(url=url,headers=header)
        info = response.text
        if "退出" in info:
         print("登陆成功")  
         pattern = re.compile(r"discuz_uid = '(.*?)'")
         matches = pattern.findall(response.text)
         uid = str(matches[0])
         sicxs_task(cookie)
         time.sleep(5)
         my(cookie,uid)
        else:
         print("登录失败")
     except Exception as e:
          print(e)
def my(cookie,uid): #我的信息
     
     url = f'https://hostloc.com/home.php?mod=space&uid={uid}&do=profile'
     header = {
        "Connection":"keep-alive",
        "authority":"hostloc.com",
        "method":"GET",
        "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "referer":"https://hostloc.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0",
        "content-type": "text/html; charset=utf-8",
        "cookie":cookie
    }
     
    
     try:
        response = s.get(url=url,headers=header)
        pattern = re.compile(r'title="访问我的空间">(.*?)</a>')
        pattern2 = re.compile(r'<li><em>积分</em>(.*?)</li><li><em>威望</em>(.*?) </li>')
        pattern3 = re.compile(r'<li><em>金钱</em>(.*?) </li>')

    

        matches = pattern.findall(response.text)
        matches1 = pattern2.findall(response.text)
        matches2 = pattern3.findall(response.text)
        # print(matches)
        # print(matches1)
        # print(matches2)

        print( "用户名：" + matches[0] + " 积分：" + matches1[0][0] + " 威望：" + matches1[0][1] + " 金钱：" + matches2[0])
     except Exception as e:
          print(e)
def sicxs_task(cookie):#任务
      uuid = random.randint(0, 12345)
      url = f'https://hostloc.com/space-uid-{uuid}.html'
      header = {      
        "Connection":"keep-alive",
        "authority":"hostloc.com",
        "method":"GET",
        "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0",
        "content-type": "text/html; charset=utf-8",
        "cookie":cookie         
     } 
      response = s.get(url=url,headers=header)
      info = response.text
      if "个人资料"in info:
          print(f"访问随机用户成功")
      elif "您指定的用户空间不存在" in info:
          print("访问失败，重试中")
          sicxs_task(cookie)
      else:
          print("失败")
def sicxs():
    if os.environ.get("hostloc"):
        ck = os.environ.get("hostloc")
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
  index(cookie)              
