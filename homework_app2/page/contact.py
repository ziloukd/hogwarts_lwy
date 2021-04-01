# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     contact
   Description :
   Author :       mi
   date：          2021/4/1
-------------------------------------------------
   Change Activity:
                   2021/4/1:
-------------------------------------------------
"""
__author__ = 'mi'

from homework_app2.page.base_page import BasePage
from homework_app2.page.member_invite_menu import MemberInviteMenu


class Contact(BasePage):
    def goto_member_invite_menu(self):
        self.steps('../page_driver/member_invite_menu.yaml')
        return MemberInviteMenu(self._driver)