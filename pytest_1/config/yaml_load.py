#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/4/17 12:59
# @Author  : Wind
# @File    : yaml_load.py
# @Software: PyCharm

import yaml


def loadYaml(loc):
    data = open(loc, "r", encoding="utf-8")
    return yaml.load(data, Loader=yaml.FullLoader)


# if __name__ == '__main__':
#     print(loadYaml("../data/txt.yaml"))
