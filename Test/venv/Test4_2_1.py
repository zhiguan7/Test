#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/4/19 15:27
# @Author  : Wind
# @File    : Test4_2_1.py
# @Software: PyCharm

## 斐波那契数列


#
rabbit_num = [1, 1]

month = 8

i = 2
while i < month:
    if month > 2:
        rabbit_num.append(rabbit_num[0] + rabbit_num[1]) ##在后面增加第一个数与第二个数的和
        del rabbit_num[0]   ## 删除第一个数
    else:
        break
    i += 1

print(rabbit_num[1])
