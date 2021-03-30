# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     contact_edit
   Description :
   Author :       mi
   date：          2021/3/30
-------------------------------------------------
   Change Activity:
                   2021/3/30:
-------------------------------------------------
"""
__author__ = 'mi'
from homework_app1.page.base_page import BasePage


class ContactEdit(BasePage):
    def delete_member(self):
        self.steps('../page/delete_test.yaml')
        from homework_app1.page.enterprise_contact import EnterpriseContact
        return EnterpriseContact(self._driver)