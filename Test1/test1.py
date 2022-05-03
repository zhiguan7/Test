#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/12/16 19:58
# @Author  : Wind
# @File    : test1.py
# @Software: PyCharm

def func(n,m):
    if(m == 1): return 1
    elif (n == 1): return 1
    elif(n == m): return 1
    else: return func(n-1,m-1)+m*func(n-1,m)

if __name__ == '__main__':
    n = int(input("输入一个大于0的整数n：")) #表示n个元素
    if(n<=0):
        print("错误输入")
    else:
        m = int(input("输入一个大于0小于大于n的整数m：")) #表示m个非空子集
        if (n <= 0 or m>n):
            print("错误输入")
        else:
            i = 1
            while(i<=n):
                sum = 0
                sum += func(n,m)
                i += 1
            print("结果：" + str(sum))
            input()