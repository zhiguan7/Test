#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/4/27 12:55
# @Author  : Wind
# @File    : crawler_.py
# @Software: PyCharm

import requests
import getpass
import json
import re
from PIL import Image
from selenium import webdriver
from bs4 import BeautifulSoup


def parse_post_url(url, headers, valcode, data):
    # 发送post请求
    return requests.post(url, headers=headers, data=data, cookies=requests.utils.dict_from_cookiejar(valcode.cookies))


def parse_get_url(url, headers):
    # 发送get请求
    return requests.get(url, headers=headers)


def main():
    """登陆地址"""
    url_1 = "http://jxgl.wyu.edu.cn/new/login"
    """验证码图片地址"""
    url_2 = "http://jxgl.wyu.edu.cn/yzm?d=1556341812068"
    """成绩单地址"""
    url_3 = "http://jxgl.wyu.edu.cn/xskccjxx!getDataList.action"
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0"}

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
               "Referer": "http://jxgl.wyu.edu.cn/xskccjxx!xskccjList.action?firstquery=1"
               }

    # 表单提交数据
    data = {}
    data["account"] = "3117001297"
    data["pwd"] = ""####################################

    # 获取验证码并保存
    img = parse_get_url(url_2, header)
    with open("yzm.jpg", "wb") as temp:
        temp.write(img.content)
    yzm = Image.open("yzm.jpg")
    yzm.show()
    data["verifycode"] = input("请输入验证码：")

    # 提交表单请求
    r = parse_post_url(url_1, header, img, data)
    # print(r.content.decode("utf-8"))
    # print(r.cookies)
    # 启动浏览器
    # driver = webdriver.Firefox()
    # driver.add_cookie(r.cookies)
    # driver.get(url_3)
    # print(driver.page_source)
    # driver.close()

    r = parse_post_url(url_3, header, img, data).content.decode("utf-8")

    # 保存为json文件
    with open("achievement.json", "w", encoding="utf-8") as temp:
        temp.write(r)

    # 处理数据
    # with open("achievement.json") as temp:
    #     data = temp.read()


if __name__ == '__main__':
    main()
