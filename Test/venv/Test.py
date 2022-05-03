#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/4/22  11:25
# @Author  : Wind
# @File    : Test.py
# @Software: PyCharm


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
    try :
        user_file = open("user.data")
        # print(users_data)
        users_data = eval(user_file.read())
    except BaseException:
        print("Error")
        exit(0)
    finally:
        user_file.close()


def read_student_file():
    """读取学员的数据"""
    global students_data
    try:
        student_file = open("student.data", "r")
        students_data = eval(student_file.read())
    except BaseException:
        print("Error")
        exit(0)
    finally:
        student_file.close()


def student_view():
    """操作界面"""
    print("----------------------------")
    print("本学员管理系统可完成如下操作：")
    print("\t1.添加学生信息")
    print("\t2.修改学生信息")
    print("\t3.删除学生信息")
    print("\t4.打印所有学生信息")
    print("\t5.打印学生信息")
    print("\t6.排序学生信息")
    print("\t7.保存学生信息")
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
            if ensure == "Y" or ensure == "y":
                del students_data[index]
                print("删除成功\n")
                break
            else:
                print("取消\n")
                break
        index += 1

    if not find_out:
        print("没有找到该学生，请重试\n")


def query_all_student_data():
    """查询所有学生信息"""
    print("- - - - -查询所有学生信息- - - - -")
    # 打印全部学生信息
    print("姓名\t性别\t年龄\t联系方式")
    for temp in students_data:
        # print(type(temp))
        print("%s\t%s\t%s\t\t%s" % (temp["name"], temp["sex"], temp["age"], temp["tel"]))
    print("打印成功\n")


def query_student_data():
    """查询指定学生信息"""
    print("- - - - -查询指定学生信息- - - - -")
    name = input("输入要查询的学生姓名：")
    index = 0
    for temp in students_data:
        if temp["name"] == name:
            find_out = True
            print("姓名\t性别\t年龄\t联系方式")
            print("%s\t%s\t%s\t\t%s" % (
            students_data[index]["name"], students_data[index]["sex"], students_data[index]["age"],
            students_data[index]["tel"]))
            print("打印成功\n")
            break
        index += 1
    if not find_out:
        print("没有找到该学生，请重试\n")


def sotf_student_data():
    """"按年龄排序学生信息"""
    print("- - - - -按年龄排序学生信息- - - - -")
    print("-------------------")
    print("选择升降序：")
    print("\t1.升序")
    print("\t2.降序")
    print("-------------------")
    is_reverse = input("输入操作：")
    data = []
    is_sort = False
    if is_reverse == "1":
        data = sorted(students_data, key=lambda x: (x['age'], x['name'], x["sex"], x["tel"]))  ##网上寻找的方法
        # print(data)
        is_sort = True
    elif is_reverse == "2":
        data = sorted(students_data, key=lambda x: (x['age'], x['name'], x["sex"], x["tel"]), reverse=True)
        #print(data)
        is_sort = True
    else:
        print("无此操作\n")

    if is_sort:
        index = 0
        while index < len(data):
            students_data[index] = data[index]
            index += 1
        print("排序成功\n")


def sava_student_data():
    """"保存学生信息"""
    print("- - - - -保存学生信息- - - - -")
    with open("student.data", "w") as write_student_file:
        # print(type(students_data))
        write_student_file.write(str(students_data))
    print("保存成功\n")


def main():
    """主函数"""
    print("- - - - -简易学生管理系统- - - - -")
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
                query_all_student_data()
            elif num == "5":
                query_student_data()
            elif num == "6":
                sotf_student_data()
            elif num == "7":
                sava_student_data()
            elif num == "0":
                print("退出系统...")
                break;
            else:
                print("无更多操作...请重新输入")


main()
