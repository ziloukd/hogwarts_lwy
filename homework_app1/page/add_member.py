# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     add_member
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


class AddMember(BasePage):
    def add_member(self):
        self.steps("../page/add_member.yaml")

        result = self.find('xpath', '//*[@class="android.widget.Toast"]').text
        return result