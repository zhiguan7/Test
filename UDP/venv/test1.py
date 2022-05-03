#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/15 14:28
# @Author  : Wind
# @File    : test_1.py
# @Software: PyCharm


 ## sample语言单词识别
keywords = ("char","int","float","break","const","return","void","continue","do","while","if","else","for")  ## 关键字
operator = ("(",")","[","]","!","*","/","%","+","-","<","<=",">",">=","==","!=","&&","||","=",".")  ## 运算符
delimiters = ("{","}",",",";") ## 界符

 ## k:关键字 o:运算符 p:界符
def func1(str): ##识别
    length = len(str) ## 字符串长度
    sign = [0]  ## 记录运算符和界符的位置
    word_list = []  ## 记录分割后的词
    list = []  ## 记录词法分析的结果
    str2 = str

    ## 先分析出运算符和界符
    index = 0
    while(index<length):
        i = index
        while(str[i] in operator or str[i] in delimiters or str[i] == " "):
            sign.append(i)
            i +=1
        s = str[index:i]
        s = s.replace(" ","")
        if(s!=""):
            list.append("(s,\"" +s+ "\")")
        index = i
        index += 1

    sign.append(length)
    length = len(sign)-1

    ## 以运算符和界符为分割点进行切割
    index = 0
    while(index < length):
        word_list.append(str[sign[index]:sign[index+1]])
        sign[index+1] += 1
        index += 1

    c_list = []
    for str in word_list:
        str = str.split()
        if(str):
            c_list.append(len(str))

    str1 = " ".join(word_list)
    word_list = str1.split()

    w_list = [] ## 记录每个词的类型
    index = 0
    i = 0
    for str in word_list:
        if (str[0].isdigit()):
            flag = func2(str)
            if (flag == 1 or flag == 2 or flag == 3):## 数字
                w_list.append("400")
            else:## 识别错误
                w_list.append("error")
        else:
            flag = func3(str)
            if(flag == 1): ## 关键字
                w_list.append("k")
            elif(flag == 2): ## 标识符
                w_list.append("700")
            else: ## 识别错误
                w_list.append("error")
        i += 1
        index += 1

    ##组合
    index = 0
    i = 0
    for c in c_list:
         while(c>0):
            list.insert(index, "(" + w_list[i] + ",\"" + word_list[i] + "\")")
            i += 1
            index += 1
            c-=1
         index +=1

    for i in list:
        print(i)


def func2(str): ## 整数识别
    alp_hex = ("a","b","c","d","e","f","A","B","C","D","E","F")
    state = '0'  ##初始状态
    length = len(str)
    index = 0
    while(state != '2'and state != '4'and state != '7'):
        if(state == '0'):
            if(str[index] == "0"):
                state = '3'
            elif(str[index].isdigit() and str[index]!="0"):
                state = '1'
        elif(state == '1'):
            if(state == '0'.isdigit()):
                state = '1'
            else: state = '2'
        elif(state == '3'):
            if(str[index].isdigit()and str[index]!="8"and str[index]!="9"):
                state = '3'
            elif(str[index] == "X" or str[index] == "x"):
                state = '5'
            else:
                state = "4"
        elif(state == "5"):
            if(str[index].isdigit() or str[index] in alp_hex):
                state = '6'
            else: break
        elif(state == '6'):
            if (str[index].isdigit() or str[index] in alp_hex):
                state = '6'
            else:
                state = '7'

        if (index == length - 1): break
        index +=1
    if(state == '1'): ## 识别为十进制数
        return 1
    elif(state == '3'): ## 识别为八进制数
        return 2
    elif(state == '6'): ## 识别为十六进制数
        return 3
    else: return 4 ## 识别错误

def func3(str): ## 标识符识别
    if(str in keywords): ## 识别出为关键字
        return 1
    state = '0' ##初始状态
    length = len(str)
    index = 0
    while(state != '2'):
        if(state == '0'):
            if(str[index].isalpha()): state = '1'
            else: break
        elif(state == '1'):
            if(str[index].isalpha() or str[index].isdigit()):
                state = '1'
            else:
                state = '2'
                break

        if(index==length-1): break
        index += 1
    if(state=='1'): ## 识别出为标识符
        return 2
    else: return 3  ## 识别错误

if __name__ == '__main__':
    #str = input("请输入一个字符串:")
    str = "els@e     if(r>= 2.0) {C = 2*pi*r"  ##测试
    func1(str)