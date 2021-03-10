# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     base_page
   Description :
   Author :       mi
   date：          2021/3/1
-------------------------------------------------
   Change Activity:
                   2021/3/1:
-------------------------------------------------
"""
__author__ = 'mi'

import shelve

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    _base_url = ""

    def __init__(self, driver: webdriver = None, debug=False):
        self._driver = driver
        self._option = None

        if debug:
            self._option = webdriver.ChromeOptions()
            self._option.debugger_address = "127.0.0.1:9222"

        if driver is None:
            self._driver = webdriver.Chrome(options=self._option)

        if self._base_url != "":
            self._driver.get(self._base_url)

    def find(self, by, locator):
        return self._driver.find_element(by, locator)

    def finds(self, by, locator):
        return self._driver.find_elements(by, locator)

    def get_cookies(self):
        cookies = self._driver.get_cookies()
        data = shelve.open('../data/cookies')
        data["cookies"] = cookies
        data.close()

    def wait(self, timeout=10):
        return WebDriverWait(self._driver, timeout=timeout)