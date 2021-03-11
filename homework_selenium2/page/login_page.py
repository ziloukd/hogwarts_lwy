# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     login
   Description :
   Author :       mi
   date：          2021/3/2
-------------------------------------------------
   Change Activity:
                   2021/3/2:
-------------------------------------------------
"""
__author__ = 'mi'

import shelve

from selenium.webdriver.common.by import By

from homework_selenium2.page.base_page import BasePage
from homework_selenium2.page.main_page import MainPage
from homework_selenium2.page.register_page import RegisterPage


class LoginPage(BasePage):
    # _base_url = "https://work.weixin.qq.com/wework_admin/frame"

    def goto_register(self):
        self.find(By.CSS_SELECTOR, ".login_registerBar_link").click()
        return RegisterPage(self._driver)

    def login_by_cookies(self):
        # 读取cookies
        data = shelve.open("../data/cookies")
        cookies = data["cookies"]
        data.close()

        # 登录
        for cookie in cookies:
            if "expiry" in cookie.keys():
                cookie.pop("expiry")
                # print(cookie)
            self._driver.add_cookie(cookie)
        self._driver.refresh()
        return MainPage(self._driver)


if __name__ == '__main__':
    test = LoginPage()
    test.login_by_cookies()