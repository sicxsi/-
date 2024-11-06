"""
name: 音乐磁场
Author: sicxs
Date: 2024-11-2
export hifini="cookie"  @,&分割
cron: 0 5 * * *
"""
import requests
import re,os,sys
import time

def index(cookie): #验证登录
     url = 'https://www.hifini.com/index.htm'
     header = {
        "authority":"www.hifini.com",
        "method":"GET",
        "path":"/index.htm",
        "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
        "content-type": "text/html; charset=utf-8; Cache-control:private",
        "referer":"https://www.hifini.com/",
        "cookie":cookie
    }
     try:
        response = requests.get(url=url,headers=header)
        info = response.text
        if "首页" in info:
         print("登陆成功")
         sing(cookie)  
        else:
         print("登录失败")
     except Exception as e:
          print(e)
def sing(cookie):#验证是否签到
     url = 'https://www.hifini.com/sg_sign.htm'
     header = {
        "authority":"www.hifini.com",
        "method":"GET",
        "path":"/sg_sign.htm",
        "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
        "content-type": "text/html; charset=utf-8; Cache-control:private",
        "referer":"https://www.hifini.com/",
        "cookie":cookie
    }
  
     try:
        response = requests.get(url=url,headers=header)

        info = response.text

        if "已签" in info:
           print("您今天已经签到过了，请勿重复签到。")
        elif "签到" in info:
         
         pattern = re.compile(r'var sign = "(.*?)"')
         matches = pattern.findall(info)
         sgin = matches[0]
         sing1(cookie,sgin)
         time.sleep(3)
         my(cookie)

        else :
          print("签到失败")

     except Exception as e:
          print(e)
def sing1(cookie,sgin):#签到
     url = 'https://www.hifini.com/sg_sign.htm'
     header = {
        "authority":"www.hifini.com",
        "method":"POST",
        "path":"/sg_sign.htm",
        "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
        "referer":"https://www.hifini.com/sg_sign.htm",
        "cookie":cookie
    }
     data = {
        "sign":sgin,
     }
     print(f"这是sgin：{sgin}")
     try:
       response = requests.post(url=url,headers=header,data=data)
       s1 = response.status_code 
       if s1 == 200 :
          print("签到成功")
       
       else:
           print("失败")
          
     except Exception as e:
         print(e)
def my(cookie):#查询信息
    url = 'https://www.hifini.com/my.htm'
    header = {
        "authority":"www.hifini.com",
        "method":"GET",
        "path":"/my.htm",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
        "referer":"https://www.hifini.com/my-post.htm",
        "cookie":cookie
    }
    try:
       response = requests.get(url=url,headers=header)
       info = response.text
       if "基本资料" in info:
         
         pattern = re.compile(r'<span class="(.*?)">(.*?)</span>')
         pattern2 = re.compile(r'金币：<em style="(.*?)">(.*?)</em> ')
         matches = pattern.findall(info)
         matches1 = pattern2.findall(info)

         #print(matches[1][1])
         #print(matches1[0][1])
         print( "用户名：" + matches[1][1] + " 金币" + matches1[0][1])
       else:
         print("？") 

    except Exception as e:
         print(e)
   

def sicxs():
    if os.environ.get("hifini"):
        ck = os.environ.get("hifini")
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