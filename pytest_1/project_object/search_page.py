#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/4/16 20:54
# @Author  : Wind
# @File    : search_page.py
# @Software: PyCharm
from selenium import webdriver
from selenium.webdriver.common.by import By

from base.base_page import BasePage


class SearchPage(BasePage):
    url = "https://www.baidu.com"
    _input = (By.ID, 'kw')
    _button = (By.ID, "su")

    def search(self, txt):
        self.visit()
        self.input_(self._input, txt)
        self.click(self._button)


# if __name__ == '__main__':
#     driver = webdriver.Firefox()
#     sp = SearchPage(driver)
#     sp.search("123")
