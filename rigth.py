"""
name: 恩山无线论坛
Author: sicxs
Date: 2024-11-3
export rigth="cookie" @,&分割
cron: 0 5 * * *
"""
import requests
import re,os,sys

def index(cookie):
     url = 'https://www.right.com.cn/forum/forum.php'
     header = {
        "Connection": "keep-alive",
        "host": "www.right.com.cn",
        "referer":"https://www.right.com.cn/forum/forum.php",
        "User-Agent": "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0",
        "content-type": "text/html; charset=utf-8",
        "cookie":cookie
    }
     try:
        response = requests.get(url=url,headers=header)
        info = response.text
        if "退出" in info:
         print("登陆成功")  
         my(cookie)
        else:
         print("登录失败")
     except Exception as e:
          print(e)
def my(cookie):
    url = "https://www.right.com.cn/forum/home.php"
    header = {
        "Connection": "keep-alive",
        "host": "www.right.com.cn",
        "referer":"https://www.right.com.cn/forum/home.php",
        "User-Agent": "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0",
        "content-type": "text/html; charset=utf-8",
        "cookie":cookie
    }
    try:
        response = requests.get(url=url,headers=header)
        pattern = re.compile(r'title="访问我的空间">(.*?)</a>')
        pattern2 = re.compile(r'<em>积分</em>(.*?)</li>')
        pattern3 = re.compile(r'<em>恩山币</em>(.*?) 币</li>')

    

        matches = pattern.findall(response.text)
        matches1 = pattern2.findall(response.text)
        matches2 = pattern3.findall(response.text)
        

        print( "用户名：" + matches[0] + " 积分：" + matches1[0] + " 恩山币：" + matches2[0])
    except Exception as e:
         print(e)
         
def sicxs():
    if os.environ.get("rigth"):
        ck = os.environ.get("rigth")
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