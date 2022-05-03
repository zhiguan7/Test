#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/4/19 14:15
# @Author  : Wind
# @File    : Test4_1_1.py
# @Software: PyCharm


## (1)输出“./test1”下的所有文件信息，并过滤出该目录下的所有“.txt”文件

import os

folder_name = "./file/test1"

if os.path.exists(folder_name):
    dir_list = os.listdir(folder_name)
    print(dir_list)

    d_list = []
    for temp in dir_list:
        if temp.endswith(".txt"):
            d_list.append(temp)

    print("过滤后：", end="")
    print(d_list)
else:
    print("找不到文件夹")

print()
## (2)批量重命名“.\file\test2”目录下的所有.docx结尾的文件，最终命名为“XYD出品-...”

folder_name = "./file/test2"

if os.path.exists(folder_name):
    dir_list = os.listdir(folder_name)
    print(dir_list)
    source_path = "C:/Users/14053/PycharmProjects/Test/venv/file/test2"
    i = 1
    for temp in dir_list:
        if temp.endswith(".docx"):
            new_name = source_path + "/XYD出品-" + str(i) + ".docx"
            old_name = source_path + "/" + temp
            os.rename(old_name,new_name)
            i+=1

    print("")
