#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/4/21 16:52
# @Author  : Wind
# @File    : Test1.py
# @Software: PyCharm


from tkinter import *

root = Tk()
root.title("Entry")
root.geometry("200x150")

#var = Variable()

e = Entry(root, show="*")
e.pack()
t = Text(root,height=2)
t.pack()

def func():
    var = e.get()
    t.insert("insert",var)

b = Button(root, width=20, height=2,text="UN",command=func)
b.pack()
root.mainloop()