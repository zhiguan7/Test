#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/4/23 12:59
# @Author  : Wind
# @File    : apptest.py
# @Software: PyCharm
from time import sleep

from appium import webdriver
from selenium.webdriver.common.by import By

if __name__ == '__main__':
    desired_caps = {
        'platformName': 'Android',
        'platformVersion': '6.0.1',
        'deviceName': 'mumu',
        # adb shell dumpsys window | findstr mCurrentFocus
        # adb shell monkey
        'appPackage': 'com.mihoyo.hyperion',
        'appActivity': 'com.mihoyo.hyperion.main.HyperionMainActivity',
        'noReset': True
    }
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    sleep(3)
    top = driver.find_elements(By.CLASS_NAME, 'android.widget.TextView')
    for t in top:
        print(t.text)
    sleep(6)
    driver.quit()
