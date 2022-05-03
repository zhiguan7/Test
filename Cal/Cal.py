#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/3 15:08
# @Author  : Wind
# @File    : Cal.py
# @Software: PyCharm

import sys
import Ui
import re
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

class CalMainWindow(QtWidgets.QMainWindow, Ui.Ui_CAL):

    def __init__(self, parent=None):
        super(CalMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.connecter()
        self.show()

    ##按键事件
    def psB_0(self):
        self.lineEdit.insert('0')

    def psB_1(self):
        self.lineEdit.insert('1')

    def psB_2(self):
        self.lineEdit.insert('2')

    def psB_3(self):
        self.lineEdit.insert('3')

    def psB_4(self):
        self.lineEdit.insert('4')

    def psB_5(self):
        self.lineEdit.insert('5')

    def psB_6(self):
        self.lineEdit.insert('6')

    def psB_7(self):
        self.lineEdit.insert('7')

    def psB_8(self):
        self.lineEdit.insert('8')

    def psB_9(self):
        self.lineEdit.insert('9')

    def psB_point(self):
        self.lineEdit.insert('.')

    def psB_add(self):
        self.lineEdit.insert('+')
        self.lineEdit_2.insert(self.lineEdit.text())
        self.lineEdit.clear()
    def psB_min(self):
        self.lineEdit.insert('-')
        self.lineEdit_2.insert(self.lineEdit.text())
        self.lineEdit.clear()
    def psB_mul(self):
        self.lineEdit.insert('*')
        self.lineEdit_2.insert(self.lineEdit.text())
        self.lineEdit.clear()
    def psB_div(self):
        self.lineEdit.insert('/')
        self.lineEdit_2.insert(self.lineEdit.text())
        self.lineEdit.clear()
    def psB_lbr(self):
        self.lineEdit.insert('(')
        self.lineEdit_2.insert(self.lineEdit.text())
        self.lineEdit.clear()
    def psB_rbr(self):
        self.lineEdit.insert(')')
        self.lineEdit_2.insert(self.lineEdit.text())
        self.lineEdit.clear()
    def psB_c(self):
        self.lineEdit.clear()
        self.lineEdit_2.clear()

    def psB_back(self):
        if self.lineEdit.text():
            self.lineEdit.backspace()
        else:
            self.lineEdit_2.backspace()
    ##连接按键
    def connecter(self):
        self.pushButton_0.clicked.connect(self.psB_0)
        self.pushButton_1.clicked.connect(self.psB_1)
        self.pushButton_2.clicked.connect(self.psB_2)
        self.pushButton_3.clicked.connect(self.psB_3)
        self.pushButton_4.clicked.connect(self.psB_4)
        self.pushButton_5.clicked.connect(self.psB_5)
        self.pushButton_6.clicked.connect(self.psB_6)
        self.pushButton_7.clicked.connect(self.psB_7)
        self.pushButton_8.clicked.connect(self.psB_8)
        self.pushButton_9.clicked.connect(self.psB_9)
        self.pushButton_point.clicked.connect(self.psB_point)
        self.pushButton_add.clicked.connect(self.psB_add)
        self.pushButton_min.clicked.connect(self.psB_min)
        self.pushButton_mul.clicked.connect(self.psB_mul)
        self.pushButton_div.clicked.connect(self.psB_div)
        self.pushButton_equ.clicked.connect(self.show_result)
        self.pushButton_lbr.clicked.connect(self.psB_lbr)
        self.pushButton_rbr.clicked.connect(self.psB_rbr)
        self.pushButton_c.clicked.connect(self.psB_c)
        self.pushButton_back.clicked.connect(self.psB_back)
        self.lineEdit.returnPressed.connect(self.show_result)

    ##键盘事件
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_0:
            self.lineEdit.insert('0')
        elif event.key() == Qt.Key_1:
            self.lineEdit.insert('1')
        elif event.key() == Qt.Key_2:
            self.lineEdit.insert('2')
        elif event.key() == Qt.Key_3:
            self.lineEdit.insert('3')
        elif event.key() == Qt.Key_4:
            self.lineEdit.insert('4')
        elif event.key() == Qt.Key_5:
            self.lineEdit.insert('5')
        elif event.key() == Qt.Key_6:
            self.lineEdit.insert('6')
        elif event.key() == Qt.Key_7:
            self.lineEdit.insert('7')
        elif event.key() == Qt.Key_8:
            self.lineEdit.insert('8')
        elif event.key() == Qt.Key_9:
            self.lineEdit.insert('9')
        elif event.key() == Qt.Key_Period:
            self.lineEdit.insert('.')
        elif event.key() == Qt.Key_Plus:
            self.lineEdit.insert('+')
            self.lineEdit_2.insert(self.lineEdit.text())
            self.lineEdit.clear()
        elif event.key() == Qt.Key_Minus:
            self.lineEdit.insert('-')
            self.lineEdit_2.insert(self.lineEdit.text())
            self.lineEdit.clear()
        elif event.key() == Qt.Key_Asterisk:
            self.lineEdit.insert('*')
            self.lineEdit_2.insert(self.lineEdit.text())
            self.lineEdit.clear()
        elif event.key() == Qt.Key_Slash:
            self.lineEdit.insert('/')
            self.lineEdit_2.insert(self.lineEdit.text())
            self.lineEdit.clear()
        elif event.key() == Qt.Key_ParenLeft:
            self.lineEdit.insert('(')
            self.lineEdit_2.insert(self.lineEdit.text())
            self.lineEdit.clear()
        elif event.key() == Qt.Key_ParenRight:
            self.lineEdit.insert(')')
            self.lineEdit_2.insert(self.lineEdit.text())
            self.lineEdit.clear()
        elif event.key() == Qt.Key_Delete:
            self.lineEdit.clear()
            self.lineEdit_2.clear()
        elif event.key() == Qt.Key_Backspace:
            if self.lineEdit.text():
                self.lineEdit.backspace()
            else: self.lineEdit_2.backspace()
        elif event.key() == Qt.Key_Enter:
            self.show_result()

    def show_result(self): ##输出结果
        text = self.lineEdit_2.text() + self.lineEdit.text()
        if text == "" or text == "Error!":
            self.lineEdit.clear()
            self.lineEdit_2.clear()
        else:
            try:
                self.lineEdit.setText(str(self.deal(text)))
                self.lineEdit_2.clear()
            except:
                self.lineEdit.setText('Error!')
                self.lineEdit_2.clear()

    def is_symbol(self, element): ##判断是符号还是数字
        res = False
        symbol = ['+', '-', '*', '/', '(', ')']
        if element in symbol:
            res = True
        return res

    def priority(self, top, next): ##优先级排序，1为最低，3为最高
        lv_1 = ['+', '-']
        lv_2 = ['*', '/']
        lv_3 = ['(']
        lv_4 = [')']

        if top in lv_1:
            if next in lv_2 or next in lv_3:##若栈顶符号为+或-，下一个符号为*和/或括号，返回优先级1，和他同级的就返回3
                return "1"
            else:
                return "3"

        elif top in lv_2:
            if next in lv_3:##若栈顶符号为*和/，下一个符号为括号，则返回优先级1，和他同级或的为+或-就返回3
                return "1"
            else:
                return "3"

        elif top in lv_3:
            if next in lv_4: ##若栈顶符号为括号(,下一个符号为),则返回2，其他返回1，括号优先级最高
                return"2"
            else:
                return "1"

    def calculale(self, num1, symbol, num2): ##计算
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

    def deal(self, text):
        str_1 = re.split('([ \+ \- \* \/ \( \) ])', text)  ##切割符号
        str_1 = [x.strip() for x in str_1 if x.strip() != '']  ##去空格
        if str_1[0] == "-" or str_1[0] == "+":  ##在正号或负号前加0，加号和减号前不变
            str_1.insert(0, 0)

        ##数字和符号数组
        num_stack = []
        sym_stack = []

        for ele in str_1:
            ret = self.is_symbol(ele)
            if not ret:
                num_stack.append(float(ele))  ##数字入数字栈
            else:
                while True:
                    if len(sym_stack) == 0:
                        sym_stack.append(ele)  ##符号入符号栈
                        break
                    res = self.priority(sym_stack[-1], ele)

                    if res == "1":  ##优先级最低，进入符号栈栈顶，继续下次判断
                        sym_stack.append(ele)
                        break
                    if res == "2":  ##此时为括号，删除括号
                        sym_stack.pop()
                        break
                    if res == "3":  ##优先级最高，取出符号栈栈顶和两次数字栈栈顶，运算
                        symbol = sym_stack.pop()
                        num2 = num_stack.pop()
                        num1 = num_stack.pop()
                        num_stack.append(self.calculale(num1, symbol, num2))
        else:
            while len(sym_stack) != 0: ##符号栈还有符号，继续运算
                symbol = sym_stack.pop()
                num2 = num_stack.pop()
                num1 = num_stack.pop()
                num_stack.append(self.calculale(num1, symbol, num2))
        result = num_stack.pop()
        return '{:g}'.format(result)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    cal = CalMainWindow()
    sys.exit(app.exec_())
