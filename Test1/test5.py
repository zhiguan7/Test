#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/12/23 15:33
# @Author  : Wind
# @File    : test5.py
# @Software: PyCharm

s = [] #所需时间队列
a = [] #并行机器队列

def search(x,y):
    global min_time
    if(y>=min_time): #若当前调度时间比最小调度时间大，没必要继续下去，剪枝
        return
    if(x==n): #完成任务
        if(y<min_time): #若比最低时间还低
            min_time = y
            return
    i = 0
    while(i<k):
        if(a[i]+s[x]<=min_time):
            a[i]+=s[x]
            search(x+1,max(y,a[i]))
            a[i]-=s[x]
        i+=1

if __name__ == '__main__':
    n = int(input("请输入任务数n："))
    k = int(input("请输入可并行工作的任务数k："))
    i = 0
    while(i<k):
        a.append(0)
        i+=1
    i = 0
    while(i<n):
        s.append(int(input("请输入任务"+str(i+1) +"所需的时间：")))
        i+=1
    s.sort(reverse=True)
    min_time = sum(s)
    search(0, 0)
    print(min_time)