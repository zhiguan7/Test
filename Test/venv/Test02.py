#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/4/27 11:55
# @Author  : Wind
# @File    : Test02.py
# @Software: PyCharm

from PIL import Image
import  pytesseract

img = Image.open('yzm.jpg')
print(pytesseract.image_to_string(img))