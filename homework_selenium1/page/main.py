# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     main
   Description :
   Author :       mi
   date：          2021/2/18
-------------------------------------------------
   Change Activity:
                   2021/2/18:
-------------------------------------------------
"""
__author__ = 'mi'

from selenium.webdriver.common.by import By

from homework_selenium1.page.base_page import BasePage
from homework_selenium1.page.login import Login
from homework_selenium1.page.register import Register


class Main(BasePage):

    _base_url = "https://work.weixin.qq.com/"

    def goto_register(self):
        self.find(By.CSS_SELECTOR,".index_head_info_pCDownloadBtn")[0].click()
        return Register(self._driver)

    def goto_login(self):
        self.find(By.CSS_SELECTOR, '.index_top_operation_loginBtn')[0].click()
        return Login(self._driver)

    def download(self):
        pass