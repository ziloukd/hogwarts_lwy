# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     app
   Description :
   Author :       mi
   date：          2021/3/31
-------------------------------------------------
   Change Activity:
                   2021/3/31:
-------------------------------------------------
"""
__author__ = 'mi'

from appium import webdriver

from homework_app2.page.base_page import BasePage
from homework_app2.page.main import Main


class App(BasePage):

    def start(self, driver=None):
        _package_name = 'com.tencent.wework'
        _app_activity = 'com.tencent.wework.launch.WwMainActivity'
        if driver is None:
            caps = {
                'platformName': 'android',
                'deviceName': 'a62c68f60406'
                 ,
                'noReset': 'true',
                'autoGrantPermissions': 'true',
                'appPackage': _package_name,
                'appActivity': _app_activity,
            }
            self._driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)
            self._driver.implicitly_wait(3)
        else:
            self._driver.start_activity(_package_name, _app_activity)

        return self

    def main(self):
        return Main(self._driver)
