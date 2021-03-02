# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     index
   Description :
   Author :       mi
   date：          2021/3/2
-------------------------------------------------
   Change Activity:
                   2021/3/2:
-------------------------------------------------
"""
__author__ = 'mi'

from selenium.webdriver.common.by import By

from homework_selenium1.page.register import Register
from homework_selenium2.page.base_page import BasePage
from homework_selenium2.page.login_page import LoginPage


class IndexPage(BasePage):
    #_base_url = ""

    def goto_login(self):
        self.find(By.CSS_SELECTOR, ".index_top_operation_loginBtn").click()
        return LoginPage(self._driver)

    def goto_register(self):
        self.find(By.CSS_SELECTOR, ".index_head_info_pCDownloadBtn")
        return Register(self._driver)