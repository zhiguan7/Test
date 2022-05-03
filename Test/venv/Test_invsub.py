#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/5/15 20:23
# @Author  : Wind
# @File    : Test_invsub.py
# @Software: PyCharm

import requests
from selenium import webdriver
from random import randint
from time import *

url = "https://www.wjx.cn/jq/39546276.aspx"

proxy = '171.80.115.248:9999'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=http://' + proxy)
c = webdriver.Chrome(chrome_options=chrome_options)

c.get("http://httpbin.org/ip")
print(c.page_source)

#添加Cookie
#temp = str(int(time()*1000))
#Cookie = "acw_tc=2f624a0415578914998515667e754c6c49016c9ebb00ffdac8c6710d725b26; .ASPXANONYMOUS=xF8yemFB1QEkAAAAMTFmNjgwYjUtMTZkMi00MDk5LWE3NjQtZWQ4MjQxNzZmOWMyDmPP1LQQLWEKiEwZJuIxoUKgwiA1; UM_distinctid=16ab991bd2c72f-03adc7ecb39082-6353160-144000-16ab991bd2d597; CNZZDATA4478442=cnzz_eid%3D171600330-1557890991-%26ntime%3D1557915797; Hm_lvt_21be24c80829bd7a683b2c536fcf520b=1557891497,1557894874,1557919490; LastActivityJoin=39546276,102716219810; jac39546276=82187725; Hm_lpvt_21be24c80829bd7a683b2c536fcf520b=" + temp,

for count in range(3):
    c.get(url)
    #第一题
    r_1 = randint(1,2)
    c.find_element_by_class_name("ulradiocheck").find_element_by_xpath("//li/a[@rel=q1_%s]"%r_1)

    #第二题
   # r_2 = randint(1,4)
   # c.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div[2]/fieldset/div[2]/div[2]/ul/li[%s]/a"%r_2).click()

    #提交键
   # c.find_element_by_xpath('//*[@id="submit_button"]').click()
   # print(count)
   # sleep(10)

