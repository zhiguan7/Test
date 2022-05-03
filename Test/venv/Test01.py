#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/4/25 18:05
# @Author  : Wind
# @File    : Test01.py
# @Software: PyCharm

import requests
import bs4

def parse_get_url(url,headers):
    return requests.get(url,headers=headers)

def main():
    #设置目标链接
    targer_url = "https://www.gamersky.com/handbook/201712/988533.shtml"
    #设置头
    headers = { "User-Agent":
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"}
    #获取html
    s = parse_get_url(targer_url,headers).content.decode("utf-8")
    #with open("3.html", "w", encoding="utf-8") as html:
    #html.write(s)
    #獲取圖片
    soup = bs4.BeautifulSoup(s,"lxml")
    #遍历图片
    index = 1
    for td in soup.find(class_ = 'table2').find('tbody').find_all('img'):
        #获取图片地址
        pic_url = td.get('data-src')
        #print(pic_url)
        #获取图片
        pic = parse_get_url(pic_url, headers)
        #print(pic)
        #设置保存地址
        save_path = "./pic/%d.jpg" %index
        #保存

        with open(save_path,"wb") as temp:
            temp.write(pic.content)
        index+=1


if __name__ == '__main__':
    main()

