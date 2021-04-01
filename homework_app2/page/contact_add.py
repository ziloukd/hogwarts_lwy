# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     contact_add
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


class ContactAdd(BasePage):
    def add_member(self):
        self.steps('../page_driver/add_member.yaml')

        from homework_app2.page.member_invite_menu import MemberInviteMenu
        return MemberInviteMenu(self._driver)