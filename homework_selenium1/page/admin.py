# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     admin
   Description :
   Author :       mi
   date：          2021/2/19
-------------------------------------------------
   Change Activity:
                   2021/2/19:
-------------------------------------------------
"""
__author__ = 'mi'

from selenium.webdriver.common.by import By

from homework_selenium1.page.add_member import AddMember
from homework_selenium1.page.base_page import BasePage


class Admin(BasePage):

    def goto_addmember(self):
        cookies = self._driver.get_cookies()

        self.find(By.CSS_SELECTOR, ".index_service_cnt_item_title")[0].click()
        return AddMember(self._driver)

if __name__ == '__main__':
    Admin(debug=True).goto_addmember()