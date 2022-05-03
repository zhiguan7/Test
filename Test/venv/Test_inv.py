#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/5/15 11:36
# @Author  : Wind
# @File    : Test_inv.py
# @Software: PyCharm

import requests
from random import randint, random
from time import *

qid = str(39546276)
rnqian = str(454807971.21085583)
for i in range(5):
    sleep(1)
    ip = str(randint(1, 8)) + "." + str(randint(1, 8)) + "." + str(randint(1, 8)) + "." + str(randint(1, 8))
    sleep(1)
    timec = str(int(time() * 1000))
    url = 'https://www.wjx.cn/joinnew/processjq.ashx?submittype=1&curID=' + qid + '&t=' + timec + '&starttime=' + (str(strftime("%Y/%m/%d%H:%M:%S", localtime())).replace('/', '%2F')).replace(':','%3A') + "&ktimes=27"+ '&validate_text='  + '&rn=' + rnqian +"&hlv=1"+ "&jqnonce=19fa8bd5-ede8-4fd5-ac61-765f0fc9a5a5&jqsign=6%3Eaf%3Fec2*bcb%3F*3ac2*fd16*012a7ad%3Ef2f2"
    temp = str(int(time() * 1000))
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7",
        "Connection": "keep-alive",
        "Content-Length": "24",
        "X-Forwarded-For": ip,
        "Content-Type": "application/x-www-form-urlencoded",
        'Host': 'www.wjx.cn',
        "Cookie": "acw_tc=2f624a0415578914998515667e754c6c49016c9ebb00ffdac8c6710d725b26; .ASPXANONYMOUS=xF8yemFB1QEkAAAAMTFmNjgwYjUtMTZkMi00MDk5LWE3NjQtZWQ4MjQxNzZmOWMyDmPP1LQQLWEKiEwZJuIxoUKgwiA1; UM_distinctid=16ab991bd2c72f-03adc7ecb39082-6353160-144000-16ab991bd2d597; CNZZDATA4478442=cnzz_eid%3D171600330-1557890991-%26ntime%3D1557915797; Hm_lvt_21be24c80829bd7a683b2c536fcf520b=1557891497,1557894874,1557919490; LastActivityJoin=39546276,102716219810; jac39546276=82187725; Hm_lpvt_21be24c80829bd7a683b2c536fcf520b=" + temp,
        "Referer": "https://www.wjx.cn/jq/" + qid + ".aspx",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36"
    }
    data = {}
    data["submitdata"] = "1$%s}2$%s" % (str(randint(1, 2)), str(randint(1, 4)))
    r = requests.post(url, data=data, headers=headers,verify=False,allow_redirects=False)
    print(r.text)
