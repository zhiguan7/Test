#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/12/17 20:48
# @Author  : Wind
# @File    : test3.py
# @Software: PyCharm

if __name__ == '__main__':
    a = input("请输入一个正整数a：")
    lens = len(a)
    if(int(a)<0): print("输入错误")
    else:
        k = int(input("请输入要删除数字的个数k："))
        if(k>lens): print("输入错误")
        else:
            c = []
            b = [] #设置两个列表存储
            for n in a:
                b.append(n) #列表b存储排序后的数列
                c.append(n) #列表b存储原来的数列
            b.sort()
            i = 0
            while(i<k):
                n = b.pop() #用n存储删除的数
                c.remove(n) #删除列表c中的n元素
                i+=1
            a = ''.join(c)
            if(a==""): print("0")
            else: print(a)