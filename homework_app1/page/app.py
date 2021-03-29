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

from homework_app1.page.base_page import BasePage
from homework_app1.page.main import Main


class App(BasePage):
    def start(self):
        _package = "com.tencent.wework"
        _appActivity = "com.tencent.wework.launch.LaunchSplashActivity"
        if self._driver is None:
            caps = {
                "platformName": "android",
                "deviceName": "lwy",
                "autoGrantPermissions": "true",
                "noReset": "true",
                "appPackage": _package,
                "appActivity": _appActivity
            }
            self._driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
            self._driver.implicitly_wait(3)
        else:
            self._driver.start_activity(_package, _appActivity)
        return self

    def main(self):
        return Main(self._driver)


if __name__ == '__main__':
    test = App()
    test.start().main().goto_contact().goto_add_member().add_member()
