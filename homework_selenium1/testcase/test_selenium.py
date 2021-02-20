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
from lxml import etree

from selenium.webdriver.common.by import By

from homework_selenium1.page.main import Main


class TestSelenium:
    def setup(self):
        self.main = Main()

    def teardown(self):
        pass

    def test_login(self):
        self.main.goto_login().scan_login()

    def test_addmember(self):
        page = self.main.goto_login().scan_login().goto_addmember().add_people()

        with open('./wechat.html', 'w', encoding='utf-8') as f1:
            f1.write(page)
        tree = etree.HTML(page)
        member_list = tree.xpath("//tr/td[2]/span/text()")
        print(member_list)
