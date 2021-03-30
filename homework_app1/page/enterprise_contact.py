# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     enterprise_contact
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
from homework_app1.page.contact_edit import ContactEdit


class EnterpriseContact(BasePage):
    def goto_contact_edit(self):
        self.steps('../page/contact_edit.yaml')
        return ContactEdit(self._driver)

    def verify_delete(self):
        try:
            self._driver.find_elements('-android uiautomator', 'new UiScrollable(new UiSelector()'
                                          '.scrollable(true).instance(0)).'
                                          'scrollIntoView(new UiSelector().'
                                          'text("张1").instance(0));')
            return "删除失败"
        except Exception as e:
            return "删除成功"
