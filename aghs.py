"""
name: 爱裹回收
Author: sicxs
Date: 2024-11-5
微信小程序
export wx_aghs="uid" @,&分割 
cron: 0 8 * * *
"""
import requests
import os,sys,time
import json

Authorization ="36656C326D706A2F53534966356161324C6236426865736562437A4F75566F41696D39614D5A4E36494A6B457652306971754643304A6E556945726F4556726754742B5645596846636F73770A564C4B6F436638375234504B6C59655036654852796E78634F6F745A784D4E58484C4D6472734E5751494776454C72773852526F705A374D65526C426B5268496B5A586435366F6A48355A500A7872786E50684953327A6D5062525A62683974654C572F61323855734F70794736347A497167516E43397555313973635738664279322B677A6D7A734B45586130536D3365736943347757420A657A5364676256344A53364C46436A4333396351337979304869515278454153654D5562386E795A56424C6E6B734335484F5A496B566258443341586646663435786E71724741424F4157770A4C75353141477A6641685555664F4E334272674731466B423268533163332B4373513359537A4734346D7637384576696C5A37375A665061326D6863493947733337432F782B45367959614A0A3654376A614A385A613446754F367253383131426D447348746F7367626B4E37614975376A7248383879525247654D3D"
def qiandao1(Authorization): #签到状态
    url = "https://alipay.haliaeetus.cn/fuli/api/fuli/signedInfo"
    header = {
            "Host": "alipay.haliaeetus.cn",
            "Connection": "keep-alive",
            "plateForm": "WX",
            "xweb_xhr": "1",
            "Authorization":Authorization,
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090c11)XWEB/11437",
            "channelNo": "",
            "Content-Type": "application/json",
            "Accept": "*/*",
            "Sec-Fetch-Site": "cross-site",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "https://servicewechat.com/wx4ff260333d3c5ddd/211/page-frame.html",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9"
            }
    try:
        response = requests.get(url=url,headers=header)
        info = json.loads(response.text)
        if 200 == info['status']:
            print(f"您已签到；{info['data']['signDays']}天")
        else:
            print("查询失败")   

    except Exception as e:
          
          print("你的账号可能到期了")    

def qiandao(Authorization): #签到
    url ="https://alipay.haliaeetus.cn/fuli/api/fuli/signed"
    header = {
        "Host": "alipay.haliaeetus.cn",
        "Connection": "keep-alive",
        "plateForm": "WX",
        "xweb_xhr": "1",
        "Authorization":Authorization,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090c11)XWEB/11437",
        "channelNo": "",
        "Content-Type": "application/json",
        "Accept": "*/*",
        "Sec-Fetch-Site": "cross-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://servicewechat.com/wx4ff260333d3c5ddd/211/page-frame.html",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9"
        }
    try:
        response = requests.get(url=url,headers=header)
        info = json.loads(response.text)
        if 200 == info['status']:
            print("签到成功")
            time.sleep(3)
            qiandao1(Authorization)
        elif 500 == info['status']:
            print("您今日已签到！")
            time.sleep(3)
            qiandao1(Authorization)
        else:
            print("签到失败")   
    except Exception as e:
          
          print("你的账号可能到期了")    
def info(Authorization):#我的信息
    url ="https://alipay.haliaeetus.cn/recy/api/auth/asset/getInfo"
    header = {
        "Host": "alipay.haliaeetus.cn",
        "Connection": "keep-alive",
        "plateForm": "WX",
        "xweb_xhr": "1",
        "Authorization":Authorization,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090c11)XWEB/11437",
        "channelNo": "",
        "Content-Type": "application/json",
        "Accept": "*/*",
        "Sec-Fetch-Site": "cross-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://servicewechat.com/wx4ff260333d3c5ddd/211/page-frame.html",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9"
        }
    try:
        response = requests.post(url=url,headers=header)
        info = json.loads(response.text)
        if 200 == info['status']:
          print(f"用户名：{info['data']['userName']}")
          time.sleep(3)
          qiandao(Authorization)
        else:
            print("失败")
    except Exception as e:
          
          print("你的账号可能到期了")    
     
def sicxs():
    if os.environ.get("wx_aghs"):
        ck = os.environ.get("wx_aghs")
    else:
        ck = ""
        if ck == "":
            print("请设置变量")

            sys.exit()

    ck_run = ck.split('@|&')

    for i, ck_run_n in enumerate(ck_run):
        print(f'\n----------- 账号【{i + 1}/{len(ck_run)}】执行 -----------')
        try:
            
            info(ck_run_n)
        except Exception as e:
            print(e)

    print(f'\n-----------  执 行  结 束 -----------')
if __name__ == '__main__':
       
 sicxs()


