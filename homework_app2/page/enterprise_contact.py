# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     enterprise_contact
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
from homework_app2.page.contact_edit import ContactEdit


class EnterpriseContact(BasePage):
    def goto_contact_edit(self):
        self.steps('../page_driver/contact_edit.yaml')
        return ContactEdit(self._driver)

    def verity_delete_member(self):
        elements = self._driver.find_elements(
            '-android uiautomator',
            'new UiScrollable(new UiSelector().'
            'scrollable(true).instance(0)).'
            'scrollIntoView(new UiSelector().'
            'text("张1").instance(0));'
        )
        if len(elements) == 0:
            return "删除成功"
        else:
            return "删除失败"