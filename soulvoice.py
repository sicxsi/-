"""
name: 铃音
Author: sicxs
Date: 2024-11-1
export soulvoice="cookie" @,&分割
cron: 0 5 * * *
"""
import requests
import re,os,sys

try:    
    from notify import send
except:pass
result = []
def index(cookie):
     url = 'https://pt.soulvoice.club/index.php'
     header = {
        "Connection": "keep-alive",
        "authority": "pt.soulvoice.club",
        "method": "GET",
        "path": "/index.php",
        "referer":"https://pt.soulvoice.club/attendance.php",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
        "content-type": "text/html; charset=utf-8; Cache-control:private",
        "cookie":cookie
    }
     try:
        response = requests.get(url=url,headers=header)
        info = response.text
        if "首页" in info:
      #   print("登陆成功")
         result.append("登陆成功\n")
         attendance(cookie)  
        else:
        # print("登录失败")
         result.append("登陆失败\n")
     except Exception as e:
          print(e)
def attendance(cookie):
     url = 'https://pt.soulvoice.club/attendance.php'
     header = {
        "Connection": "keep-alive",
        "authority": "pt.soulvoice.club",
        "method": "GET",
        "path": "/attendance.php",
        "referer":"https://pt.soulvoice.club/index.php",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
        "content-type": "text/html; charset=utf-8; Cache-control:private",
        "cookie":cookie
    }
     try:
        response = requests.get(url=url,headers=header)
        info = response.text
        if "签到成功" in info:
           
         #  print("签到成功")
           result.append("签到成功\n")

           torrents(cookie)

        elif "您今天已经签到过了" in info:
         
         #print("您今天已经签到过了，请勿重复刷新。")
         result.append("您今天已经签到过了，请勿重复刷新。\n")

         torrents(cookie)

        else :
       #   print("签到失败")
          result.append("签到失败\n")

     except Exception as e:
          print(e)
def torrents(cookie):
     url = 'https://pt.soulvoice.club/torrents.php'
     header = {
        "Connection": "keep-alive",
        "authority": "pt.soulvoice.club",
        "method": "GET",
        "path": "/torrents.php",
        "referer":"https://pt.soulvoice.club/attendance.php",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
        "content-type": "text/html; charset=utf-8; Cache-control:private",
        "cookie":cookie
    }
     try:
       response = requests.get(url=url,headers=header)
       pattern = re.compile(r"class='CrazyUser_Name'><b>(.+?)</b>")
       pattern2 = re.compile(r'>使用</a>]: (.*)                 <a')
       pattern3 = re.compile(r'签到已得(.*?)\]</a>')
    

       matches = pattern.findall(response.text)
       matches1 = pattern2.findall(response.text)
       matches2 = pattern3.findall(response.text)

       #print( "用户名：" + matches[0] + " 魔力值：" + matches1[0] + " 签到已得：" + matches2[0])
       result.append("用户名：" + matches[0] + " 魔力值：" + matches1[0] + " 签到已得：" + matches2[0])

     except Exception as e:
         print(e)

def sicxs():
    if os.environ.get("soulvoice"):
        ck = os.environ.get("soulvoice")
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

    try:    
         send("铃音",f"{''.join(result)}")
    except Exception as e:    
         print(f"消息推送失败：{e}！\n{result}\n")      
     
    print(f'\n-----------  执 行  结 束 -----------')
    
 
if __name__ == '__main__':
  
  sicxs() 
  
 