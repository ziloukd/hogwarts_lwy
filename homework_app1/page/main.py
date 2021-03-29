# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     main
   Description :
   Author :       mi
   date：          2021/3/29
-------------------------------------------------
   Change Activity:
                   2021/3/29:
-------------------------------------------------
"""
__author__ = 'mi'
from homework_app1.page.base_page import BasePage
from homework_app1.page.contact import Contact


class Main(BasePage):
    def goto_contact(self):
        self.steps("../page/main.yaml")
        return Contact(self._driver)


if __name__ == '__main__':
    from practice.app_practice.page.app import App
    test = App()