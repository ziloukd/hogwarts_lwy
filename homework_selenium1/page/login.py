# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     login
   Description :
   Author :       mi
   date：          2021/2/18
-------------------------------------------------
   Change Activity:
                   2021/2/18:
-------------------------------------------------
"""
__author__ = 'mi'

from homework_selenium1.page.base_page import BasePage
from homework_selenium1.page.register import Register


class Login(BasePage):

    # _base_url = "https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome"

    def goto_register(self):
        return Register()

    def scan(self):
        pass