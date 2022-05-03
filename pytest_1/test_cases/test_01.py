#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/4/16 21:07
# @Author  : Wind
# @File    : test_01.py
# @Software: PyCharm
from time import sleep

from selenium import webdriver
from project_object.search_page import SearchPage
from config.yaml_load import loadYaml
import pytest


class TestCase01:

    def setup_class(self) -> None:
        self.driver = webdriver.Firefox()
        self.sp = SearchPage(self.driver)

    def teardown_class(self) -> None:
        sleep(3)
        self.driver.quit()

    @pytest.mark.parametrize("txt", loadYaml("../data/txt.yaml"))
    def test_search(self, txt):
        self.sp.search(txt['str'])


if __name__ == '__main__':
    pytest.main()
