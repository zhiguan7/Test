#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/6 13:41
# @Author  : Wind
# @File    : Testeval.py
# @Software: PyCharm

import re

def is_symbol(element):  ##判断是符号还是数字
    res = False
    symbol = ['+', '-', '*', '/', '(', ')']
    if element in symbol:
        res = True
    return res


def priority(top, next):  ##优先级排序，1为最低，3为最高
    lv_1 = ['+', '-']
    lv_2 = ['*', '/']
    lv_3 = ['(']
    lv_4 = [')']

    if top in lv_1:
        if next in lv_2 or next in lv_3:  ##若栈顶符号为+或-，下一个符号为*和/或括号，返回优先级1，和他同级的就返回3
            return "<"
        else:
            return ">"

    elif top in lv_2:
        if next in lv_3:  ##若栈顶符号为*和/，下一个符号为括号，则返回优先级1，和他同级或的为+或-就返回3
            return "<"
        else:
            return ">"

    elif top in lv_3:
        if next in lv_4:  ##若栈顶符号为括号(,下一个符号为),则返回2，其他返回1，括号优先级最高
            return "="
        else:
            return "<"


def calculale(num1, symbol, num2):  ##计算
    result = 0
    if symbol == "+":
        result = num1 + num2
    elif symbol == "-":
        result = num1 - num2
    elif symbol == "*":
        result = num1 * num2
    elif symbol == "/":
        result = num1 / num2
    return result


exp = "111"

# it = [i for i in re.split('(\-\d+\.*\d*)', exp) if i]
# exp_1 = []
#
# while True:
#     if len(it) == 0:
#         break
#     exp = it.pop(0)
#     if len(exp_1) == 0 and re.search('^\-\d+\.*\d*$', exp):
#         exp_1.append(exp)
#         continue
#     if len(exp_1) > 0:
#         if re.search('[\+\-\*\/\(]$', exp_1[-1]):
#             exp_1.append(exp)
#             continue
#     new_l = [i for i in re.split('([\+\-\*\/\(\)])', exp) if i]
#     exp_1 += new_l
# print(exp_1)

# str_1 = re.split('([ \+ \- \* \/ \( \) ])', exp_1)
#
# str_1 = [x.strip() for x in str_1 if x.strip() != '']  ##去空格
# if str_1[0] == "-" or str_1[0] == "+":  ##在正号或负号前加0，加号和减号前不变
#     str_1.insert(0, 0)

exp_1 = re.split('([ \+ \- \* \/ \( \) ])', exp)  ##切割符号
exp_1 = [x.strip() for x in exp_1 if x.strip() != '']  ##去空格
if exp_1[0] == "-" or exp_1[0] == "+":  ##在正号或负号前加0，加号和减号前不变
    exp_1.insert(0, 0)

    ##数字和符号数组
num_stack = []
sym_stack = []

for ele in exp_1:
    ret = is_symbol(ele)
    if not ret:
        num_stack.append(float(ele))  ##数字入数字栈
    else:
        while True:
            if len(sym_stack) == 0:
                sym_stack.append(ele)  ##符号入符号栈
                break
            res = priority(sym_stack[-1], ele)

            if res == "<":  ##优先级最低，进入符号栈栈顶，继续下次判断
                sym_stack.append(ele)
                break
            if res == "=":  ##此时为括号，删除括号
                sym_stack.pop()
                break
            if res == ">":  ##优先级最高，取出符号栈栈顶和两次数字栈栈顶，运算
                symbol = sym_stack.pop()
                num2 = num_stack.pop()
                num1 = num_stack.pop()
                num_stack.append(calculale(num1, symbol, num2))
else:
    while len(sym_stack) != 0:
        symbol = sym_stack.pop()
        num2 = num_stack.pop()
        num1 = num_stack.pop()
        num_stack.append(calculale(num1, symbol, num2))


print(num_stack.pop(),sym_stack)


