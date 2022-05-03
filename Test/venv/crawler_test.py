#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/4/23 14:57
# @Author  : Wind
# @File    : crawler_test.py
# @Software: PyCharm

import requests
import lxml.html
import json


# 发送请求
def parse_url(url, headers):
    return requests.get(url, headers=headers).content.decode("utf-8")


def get_weather_data(html_data):
    my_etree = lxml.html.etree
    # 解析HTML网页
    data = my_etree.HTML(html_data, my_etree.HTMLParser())
    # 获取li列表中的数据
    day_list = data.xpath("//div[@class='c15d']/ul/li")
    # print(day_list)
    # print(len(day_list))
    datas = []
    for temp in day_list:
        item = {}
        item["date"] = temp.xpath("./span[@class='time']/text()")[0]
        # 打印日期
        # print(date)
        item["weather"] = temp.xpath("./span[@class='wea']/text()")[0]
        # 打印日期
        # print(weather)
        item["min_temperature"] = temp.xpath("./span[@class='tem']/text()")[0]
        item["min_temperature"] = str(item["min_temperature"])[1:]
        #print(type(item["min_temperature"]))
        item["max_temperature"] = temp.xpath("./span[@class='tem']/em/text()")[0]
        #print(type(item["max_temperature"]))
        # 打印温度
        # print("%s-%s"%(min_temperature,max_temperature))
        datas.append(item)
    # print(datas)
    return datas


def save(data):
    # 转换为json类型数据格式
    json_data = json.dumps(data, ensure_ascii=False, indent=2)
    # print(json_data)
    with open("weatherbygz.json", "w", encoding="utf-8") as file:
        file.write(json_data)

    print("保存成功\n")


def main():
    # 设置目标网络链接
    target_url = "http://www.weather.com.cn/weather15d/101280101.shtml"
    # 添加请求头
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"}

    # 1.获取网页数据
    html_data = parse_url(target_url, headers)

    # with open("1.html","w",encoding="utf-8") as html:
    #     html.write(html_data)

    # 2.提取数据（数据清洗）
    weather_datas = get_weather_data(html_data)

    # 3.保存位json文件
    save(weather_datas)


if __name__ == '__main__':
    main()
