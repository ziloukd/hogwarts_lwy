# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     base_page
   Description :
   Author :       mi
   date：          2021/2/18
-------------------------------------------------
   Change Activity:
                   2021/2/18:
-------------------------------------------------
"""
__author__ = 'mi'

import shelve

from selenium import webdriver
from selenium.webdriver.common.by import By


class BasePage:
    _base_url = ""

    def __init__(self, driver: webdriver = None, debug=False):
        self._driver = driver

        # chrome浏览器配置
        self.options = webdriver.ChromeOptions()
        if debug:
            self.options.debugger_address = "127.0.0.1:9222"
            self._driver = webdriver.Chrome(options=self.options)
        elif self._driver is None:
            self._driver = webdriver.Chrome()

        if self._base_url != "":
            self._driver.get(self._base_url)

        self._driver.implicitly_wait(10)


    def find(self, by, locator):
        return self._driver.find_elements(by, locator)

    def save_cookies(self, cookies):
        db = shelve.open('../data/cookies')
        db['cookies'] = cookies
        db.close()