# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     member_invite_menu
   Description :
   Author :       mi
   date：          2021/4/1
-------------------------------------------------
   Change Activity:
                   2021/4/1:
-------------------------------------------------
"""
__author__ = 'mi'

import time

from homework_app2.page.base_page import BasePage
from homework_app2.page.contact_add import ContactAdd


class MemberInviteMenu(BasePage):
    def goto_contact_add(self):
        self.steps('../page_driver/contact_add.yaml')
        return ContactAdd(self._driver)

    def verity_toast(self):
        return self.get_toast_text()