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

from selenium import webdriver


class BasePage:
    _base_url = ""

    def __init__(self, driver: webdriver = None, debug = False):
        self._driver = driver
        if debug:
            self._option = webdriver.ChromeOptions()
            self._option.debugger_address = "127.0.0.1:9222"

        if driver is None:
            self._driver = webdriver.Chrome()

        if self._base_url is not "":
            self._driver.get(self._base_url)

    def find(self, by, locator):
        return self._driver.find_element(by, locator)

    def finds(self, by, locator):
        return self._driver.find_elements(by, locator)