#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/5/16 10:21
# @Author  : Wind
# @File    : Test_proxy.py
# @Software: PyCharm

from selenium import webdriver

foxOptions = webdriver.FirefoxOptions()


proxy = '110.84.208.95:8118'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=http://' + proxy)
chrome = webdriver.Chrome(chrome_options=chrome_options)

# 查看本机ip，查看代理是否起作用
chrome.get("http://httpbin.org/ip")
print(chrome.page_source)

# 退出，清除浏览器缓存
chrome.quit()

"""
## 第一步：创建一个FirefoxProfile实例
profile = webdriver.FirefoxProfile()
## 第二步：开启“手动设置代理”
profile.set_preference('network.proxy.type', 1)
## 第三步：设置代理IP
profile.set_preference('network.proxy.http', '180.125.22.71')
## 第四步：设置代理端口，注意端口是int类型，不是字符串
profile.set_preference('network.proxy.http_port', 22190)
## 第五步：设置htpps协议也使用该代理
profile.set_preference('network.proxy.ssl',  '180.125.22.71')
profile.set_preference('network.proxy.ssl_port', 22190)

driver = webdriver.Firefox(profile)
driver.get('http://httpbin.org/get')
print(driver.page_source)
driver.quit()
"""
