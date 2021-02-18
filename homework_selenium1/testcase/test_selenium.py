# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test_selenium
   Description :
   Author :       mi
   date：          2021/2/18
-------------------------------------------------
   Change Activity:
                   2021/2/18:
-------------------------------------------------
"""
__author__ = 'mi'

from time import sleep

from homework_selenium1.page.main import Main


class TestSelenium:
    def setup(self):
        self.main = Main()

    def teardown(self):
        pass

    def test_register(self):
        self.main.goto_register()