# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     main
   Description :
   Author :       mi
   date：          2021/3/31
-------------------------------------------------
   Change Activity:
                   2021/3/31:
-------------------------------------------------
"""
__author__ = 'mi'

from homework_app2.page.base_page import BasePage
from homework_app2.page.contact import Contact


class Main(BasePage):
    def goto_contact(self):
        self.steps('../page_driver/contact.yaml')
        return Contact(self._driver)