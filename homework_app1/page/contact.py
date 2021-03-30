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
from homework_app1.page.enterprise_contact import EnterpriseContact


class Contact(BasePage):
    def goto_add_member(self):
        self.steps("../page/contact.yaml")
        return AddMember(self._driver)

    def goto_enterprise_contact(self):
        self.steps("../page/enterprise_contact.yaml")
        return EnterpriseContact(self._driver)

    def verity_add_member(self):
        try:
            result = self._driver.find_element('xpath', '//*[@class="android.widget.Toast"]').text
            return result
        except Exception as e:
            return "添加失败"


