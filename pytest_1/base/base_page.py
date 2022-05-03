#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/4/16 20:42
# @Author  : Wind
# @File    : base_page.py
# @Software: PyCharm

class BasePage():

    def __init__(self, driver) -> None:
        super().__init__()
        self.driver = driver

    def visit(self):
        self.driver.get(self.url)

    def locator(self, loc):
        return self.driver.find_element(*loc)

    def click(self, loc):
        self.locator(loc).click()

    def input_(self, loc, txt):
        self.locator(loc).send_keys(txt)
