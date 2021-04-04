# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     contact_edit
   Description :
   Author :       lwy
   date：          2021/4/4
-------------------------------------------------
   Change Activity:
                   2021/4/4:
-------------------------------------------------
"""
__author__ = 'lwy'

from homework_app2.page.base_page import BasePage


class ContactEdit(BasePage):
    def delete_member(self):
        self.steps('../page_driver/delete_member.yaml')

        from homework_app2.page.enterprise_contact import EnterpriseContact
        return EnterpriseContact(self._driver)
