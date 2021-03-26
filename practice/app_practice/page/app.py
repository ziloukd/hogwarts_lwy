# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     app
   Description :
   Author :       mi
   date：          2021/3/22
-------------------------------------------------
   Change Activity:
                   2021/3/22:
-------------------------------------------------
"""
__author__ = 'mi'
from appium import webdriver

from practice.app_practice.page.base_page import BasePage


class App(BasePage):
    def start(self):
        _package = "com.xueqiu.android"
        _appActivity = ".view.WelcomeActivityAlias"
        if self._driver is None:
            caps = {
                "platformName": "android",
                "deviceName": "a62c68f60406",
                "autoGrantPermissions": "true",
                "noReset": "true",
                "appPackage": _package,
                "appActivity": _appActivity
            }
            self._driver = webdriver.Remote("http://loaclhost:4723/wd/hub", caps)
            self._driver.implicitly_wait(3)
        else:
            self._driver.start_activity(_package, _appActivity)

    def