#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/5/1 10:05
# @Author  : Wind
# @File    : Test_selenium.py
# @Software: PyCharm

from selenium import webdriver
import time
#设置链接
url = "http://jxgl.wyu.edu.cn"
url_1 = "http://jxgl.wyu.edu.cn/login!welcome.action"

#启动浏览器
brower = webdriver.Firefox()

brower.get(url)

brower.add_cookie({'name':'JSESSIONID','value':'74E438F7780BDC4395A29AB82A995407'})

cookie_list=brower.get_cookies()
cookie_dict = {}
# 格式化打印cookie
for cookie in cookie_list:
    cookie_dict[cookie['name']]=cookie['value']
print(cookie_dict)

brower.get(url_1)
#隐式等待2秒
#brower.implicitly_wait(2)

#等待2秒  time.sleep()最垃圾的显式等待
time.sleep(2)
brower.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[1]/table/tbody/tr[2]/td/div/table/tbody/tr[7]/td").click()

# with open("4.html","w",encoding="utf-8") as temp:
#    temp.write(brower.page_source)

#关闭浏览器
#brower.close()
#brower.quit()
