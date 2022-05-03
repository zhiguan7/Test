#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/4/19 16:55
# @Author  : Wind
# @File    : Test4_2_2.py
# @Software: PyCharm


"""

在F盘下新建如下文件：
	F:\src\file\test5\dir1\dir2\dir2.doc
	F:\src\file\test5\dir1\dir3\dir4\dir4.doc
	F:\src\file\test5\dir1\dir1.doc
	F:\src\file\test5\dir1\source.txt
	F:\src\file\test5\dir1\test.txt
	使用递归算法输出结尾为".doc"的所有文件

"""
import os

dir_path = "./file/test5/dir1"

def fun(data_path):
    list = os.listdir(data_path)
    index = 0
    for temp in list:
        if os.path.isdir(data_path+"/"+temp):
            fun(data_path+"/"+temp)
        else:
            if temp.endswith(".doc"):
                print(temp)

fun(dir_path)