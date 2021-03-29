# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     contact
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
from homework_app1.page.add_member import AddMember


class Contact(BasePage):
    def goto_add_member(self):
        self.steps("../page/contact.yaml")
        return AddMember(self._driver)
