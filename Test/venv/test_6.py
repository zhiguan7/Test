#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/5/15 19:54
# @Author  : Wind
# @File    : test_6.py
# @Software: PyCharm

import random
import requests
import urllib.parse
import urllib.request
from PIL import Image
import pytesseract
import os
import random
from time import time,strftime, localtime
import time as t
qid=str(39546276)
rnqian=str(2063096382)
def download(qid,header,i):
        url='https://www.wjx.cn/AntiSpamImageGen.aspx?q='+qid+'&t='+str(int(time() * 1000))
        req = urllib.request.Request(url,headers=header)
        data = urllib.request.urlopen(req).read()
        pic = open('%d.gif'%(i),'wb')
        pic.write(data)
        pic.close()
def binarizing(img): #input: gray image
    threshold=30
    pixdata = img.load()
    w, h = img.size
    for y in range(h):
        for x in range(w):
            if pixdata[x, y] > threshold:
                pixdata[x, y] = 255
            else:
                pixdata[x, y] = 0
    return img
def depoint(img):   #input: gray image
    pixdata = img.load()
    w,h = img.size
    for y in range(1,h-1):
        for x in range(1,w-1):
            count = 0
            if pixdata[x,y-1] > 245:
                count = count + 1
            if pixdata[x,y+1] > 245:
                count = count + 1
            if pixdata[x-1,y] > 245:
                count = count + 1
            if pixdata[x+1,y] > 245:
                count = count + 1
            if count >2:
                pixdata[x,y] = 255
    return img
def shibie(img):
    imgry = img.convert('L')
    threshold = 140
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    out = imgry.point(table, '1')
    print(str(pytesseract.image_to_string(out)).strip())
    return(str(pytesseract.image_to_string(out)).strip())#适用于简单二维码
def post(qid,rnqian,i):
    timeg=str(int(time() * 1000))
    t.sleep(10)
    timep=str(int(time() * 1000))
    ip=str(random.randint(1,4))+'.'+str(random.randint(1,4))+'.'+str(random.randint(1,4))+'.'+str(random.randint(1,4))
    rnhou=str(random.randint(10000000,99999999))
    headerget={
        'Host': 'www.wjx.cn',
        'Connection': 'keep-alive',
        'X-Forwarded-For': ip,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)      Chrome/62.0.3202.89 Safari/537.36 EXT/6d8a2f10c62d11e7gqpxa53987ed19aa47e3/2.4',
        'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
        'Referer': 'https://www.wjx.cn/jq/'+qid+'.aspx',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cookie': '.ASPXANONYMOUS=Se6Dlf-S0wEkAAAAMzEyZGYyZmUtYzBmYi00YWM3LWIyMTEtMTEzZWI0YzkzMmZhi6xL6iHoMTghIlPoznFqbYuLd1s1; spiderregkey=www.wjx.cn%c2%a7%c2%a71; baidutgkey=%u95EE%u5377%u661FBH%7C2%7Cbaidu; _uab_collina=151065406900158178719624; SojumpSurvey=01022D8896C0612BD508FE2D28A847832BD508000670002D00740065007300740000012F00FF29B0D12A4780F0718D63D71441EC14F08F69B611;  lllogcook=1; LastCheckUpdateDate=1; ASP.NET_SessionId=4mbujabo1zx2a1imb0pw40k0; _umdata=C234BF9D3AFA6FE7FD70ECA73142BFB1DAA8AC4CAD8E980472CE17B2B4815B078B6B64C8E7D1428ACD43AD3E795C914CB6CD457CEA3135697A8EEEB6A2679E66; LastActivityJoin=16276361,101135441472; Hm_lvt_21be24c80829bd7a683b2c536fcf520b=1510624314,1510653859,1510658882,1510665316;    Hm_lpvt_21be24c80829bd7a683b2c536fcf520b='+timeg,
        'RA-Ver': '2.4',
        'RA-Sid': '6d8a2f10c62d11e7gqpxa53987ed19aa47e3',
    }
    headerpost = {
        'Host': 'www.wjx.cn',
        'Connection': 'keep-alive',
        'X-Forwarded-For': ip,
        'Origin': 'https://www.wjx.cn',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36 EXT/6d8a2f10c62d11e7gqpxa53987ed19aa47e3/2.4',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': '*/*',
        'Referer': 'https://www.wjx.cn/jq/'+qid+'.aspx',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cookie': '.ASPXANONYMOUS=Se6Dlf-S0wEkAAAAMzEyZGYyZmUtYzBmYi00YWM3LWIyMTEtMTEzZWI0YzkzMmZhi6xL6iHoMTghIlPoznFqbYuLd1s1; spiderregkey=www.wjx.cn%c2%a7%c2%a71; baidutgkey=%u95EE%u5377%u661FBH%7C2%7Cbaidu; _uab_collina=151065406900158178719624; SojumpSurvey=01022D8896C0612BD508FE2D28A847832BD508000670002D00740065007300740000012F00FF29B0D12A4780F0718D63D71441EC14F08F69B611; lllogcook=1; LastCheckUpdateDate=1; ASP.NET_SessionId=4mbujabo1zx2a1imb0pw40k0; LastActivityJoin=16276361,101135464182; _umdata=C234BF9D3AFA6FE7FD70ECA73142BFB1DAA8AC4CAD8E980472CE17B2B4815B078B6B64C8E7D1428ACD43AD3E795C914CB6CD457CEA3135697A8EEEB6A2679E66; Hm_lvt_21be24c80829bd7a683b2c536fcf520b=1510624314,1510653859,1510658882,1510665316; Hm_lpvt_21be24c80829bd7a683b2c536fcf520b='+timep,
        'RA-Ver': '2.4',
        'RA-Sid': '6d8a2f10c62d11e7gqpxa53987ed19aa47e3',
    }
    download(qid,headerget,i)
    t.sleep(5)
    img = Image.open('%d.gif'%(i)).convert("L")
    img = binarizing(img)
    img = depoint(img)
    yanzhengma=shibie(img)
    timec=str(int(time() * 1000))
    thedata = {'submitdata': '1$'+str(random.randint(1,5))+'}2$'+str(random.randint(1,10))+'}3$'+str(random.randint(1,3))+'}4$'+str(random.randint(1,4))+'}5$1<'+str(random.randint(1,9))+',2<'+str(random.randint(1,5))+',3<'+str(random.randint(1,5))+',4<'+str(random.randint(1,5))+',5<'+str(random.randint(1,5))+',6<'+str(random.randint(1,5))+',7<'+str(random.randint(1,5))+',8<'+str(random.randint(1,5))+',9<'+str(random.randint(1,5))+'}6$'+str(random.randint(1,3))+'}7$'+str(random.randint(1,7))+'}8$'+str(random.randint(1,3))+'|'+str(random.randint(3,6))+'|'+str(random.randint(7,9))+'}9$'+str(random.randint(1,4))+'|'+str(random.randint(5,7))+'}10$'+str(random.randint(1,3))+'}11$'+str(random.randint(1,4))+'}12$1<1,2<4,3<6,4<3,5<8,6<3,7<6,8<5}13$'+str(random.randint(1,4))+'|'+str(random.randint(5,7))+'}14$2|5}15$'+str(random.randint(1,2))+'}16$'+str(random.randint(1,2))+'}17$'+str(random.randint(1,2))+'}18$'+str(random.randint(1,2))+'}19$'+str(random.randint(1,2))+'}20$'+str(random.randint(1,4))+'}21$'+str(random.randint(1,3))}
    url1='https://www.wjx.cn/handler/processjq.ashx?submittype=1&curID='+qid+'&t='+timec+'&starttime='+(str(strftime("%Y/%m/%d%H:%M:%S", localtime())).replace('/','%2F')).replace(':','%3A')+'&validate_text='+str(yanzhengma)+'&rn='+rnqian+'&sd='+('https://www.wjx.cn/'.replace('/','%2F')).replace(':','%3A')
#改rn
    t.sleep(10)

    r = requests.post(url1, headers = headerpost,data = thedata,allow_redirects=False)
    print(r.text)
main(qid,rnqian)
