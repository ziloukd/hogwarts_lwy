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

from selenium import webdriver
from selenium.webdriver.common.by import By


class BasePage:
    _base_url = ""

    def __init__(self, driver: webdriver = None):
        if self._driver is None:
            self._driver = webdriver.Chrome()
        else:
            self._driver = driver
        if self._base_url != "":
            self._driver.get(self._base_url)

    def find(self, by, locator):
        return self._driver.find_element(locator, by)
