#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/4/22 15:14
# @Author  : Wind
# @File    : TestGUI.py
# @Software: PyCharm

from tkinter import *

users_data = []
students_data = []


def user_login():
    """管理员登陆"""

    user_name = input("输入用户名：")
    password = input("输入密码：")
    for user in users_data:
        if user["username"] == user_name and user["password"] == password:
            return True
    return False


def read_user_file():
    """读取管理员的数据"""
    global users_data
    with open("user.data") as user_file:
        # print(users_data)
        users_data = eval(user_file.read())


def read_student_file():
    """读取学员的数据"""
    global students_data
    with open("student.data","r") as student_file:
        students_data = eval(student_file.read())


def student_view():
    """操作界面"""
    print("----------------------------")
    print("本学员管理系统可完成如下操作：")
    print("\t1.添加学生")
    print("\t2.修改学生")
    print("\t3.删除学生")
    print("\t4.查询学生")
    print("\t5.保存信息")
    print("\t0.退出系统")
    print("----------------------------")


def add_student_data():
    """增加学生信息"""
    print("- - - - -增加学生信息- - - - -")
    name = input("输入学生姓名：")
    sex = input("输入学生性别：")
    age = input("输入学生年龄：")
    tel = input("输入学生联系方式：")
    data = {"name": name, "sex": sex, "age": age, "tel": tel}
    students_data.append(data)
    print("新增成功\n")


def updata_student_data():
    """更新学生信息"""
    print("- - - - -更新学生信息- - - - -")
    find_out = False

    name = input("输入要更新的学生姓名：")
    index = 0
    for temp in students_data:
        if temp["name"] == name:
            find_out = True
            sex = input("请输入学生性别：")
            age = input("请输入学生年龄：")
            tel = input("请输入学生联系方式：")
            students_data[index]["name"] = name
            students_data[index]["sex"] = sex
            students_data[index]["age"] = age
            students_data[index]["tel"] = tel
            print("更新成功\n")
            break
        index += 1
    if not find_out:
        print("没有找到该学生，请重试\n")


def del_student_data():
    """删除学生信息"""
    print("- - - - -删除学生信息- - - - -")
    find_out = False

    name = input("输入要删除的学生姓名：")
    index = 0
    for temp in students_data:
        if temp["name"] == name:
            find_out = True
            ensure = input("确定要删除该学生信息?(Y/N)")
            if ensure =="Y" or ensure == "y":
                del students_data[index]
                print("删除成功\n")
                break
            else:
                print("取消\n")
                break
        index += 1

    if not find_out:
        print("没有找到该学生，请重试\n")


def query_student_data():
    """查询学生信息"""
    print("- - - - -查询学生信息- - - - -")
    # 打印全部学生信息
    print("姓名\t性别\t年龄\t联系方式")
    for temp in students_data:
        # print(type(temp))
        print("%s\t%s\t%s\t\t%s" % (temp["name"], temp["sex"], temp["age"], temp["tel"]))
    print("打印成功\n")


def sava_student_data():
    """"保存学生信息"""
    print("- - - - -保存学生信息- - - - -")
    with open("student.data","w") as write_student_file:
        #print(type(students_data))
        write_student_file.write(str(students_data))
    print("保存成功\n")





root = Tk()
root.title("Simple Students Manager")
root.geometry("400x300")
Text(root)
user = Entry(root)
user.pack()

pwd = Entry(root, show="*")
pwd.pack()

cb = Checkbutton(root)
cb.pack()

def func():
    # 读取文件
    read_user_file()

    # 判断登陆次数
    count = 0
    while count < 3:
        # 判断用户名与密码是否正确
        if user_login():
            break;
        else:
            print("用户名或密码错误,还可尝试%d次" % (2 - count))
        count += 1
    if count >= 3:
        print("登陆失败")
    else:
        # 显示操作界面
        student_view()
        # 读取文件
        read_student_file()
        while True:
            # 操作数
            num = input("输入操作：")

            # 判断要执行的操作
            if num == "1":
                add_student_data()
            elif num == "2":
                updata_student_data()
            elif num == "3":
                del_student_data()
            elif num == "4":
                query_student_data()
            elif num == "5":
                sava_student_data()
            elif num == "0":
                print("退出系统...")
                break;
            else:
                print("无更多操作...请重新输入")

b = Button(root, width=20, height=2,text="Login In",command=func)
b.pack()


root.mainloop()