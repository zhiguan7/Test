#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/4/27 19:16
# @Author  : Wind
# @File    : Test3.py
# @Software: PyCharm

import json

with open("achievement.json",encoding="utf-8") as temp:
    data = json.loads(temp.readline())

