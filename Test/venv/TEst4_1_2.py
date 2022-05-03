#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/4/19 15:08
# @Author  : Wind
# @File    : TEst4_1_2.py
# @Software: PyCharm

## （1）将noBug.txt纯文本文件拷贝至F:\src\file\test3目录下，并命名为noBug_copy.txt

with open("./file/test3/noBug.txt",encoding="utf-8") as file01:
    with open("./file/test3/noBug_copy.txt","w",encoding="utf-8") as file02:
        file02.writelines(file01.readlines())

print("拷贝完毕")

## （2）将insertsort.wmv视频文件拷贝至F:\src\file\file\test4目录下，并命名为insertsort_copy.wmv

file03 = open("./file/test4/insertsort.wmv","rb")

file04 = open("./file/test4/insertsort_copy.wmv","wb")

file04.write(file03.read())

file04.close()

file03.close()

print("拷贝完毕")