# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     add_member
   Description :
   Author :       mi
   date：          2021/2/19
-------------------------------------------------
   Change Activity:
                   2021/2/19:
-------------------------------------------------
"""
__author__ = 'mi'

import shelve

from selenium.webdriver.common.by import By

from homework_selenium1.page.base_page import BasePage


class AddMember(BasePage):

    # _base_url = "https://work.weixin.qq.com/wework_admin/frame#contacts"

    def add_people(self):
        """
        添加成员
        :return:
        """
        self.find(By.ID, "username")[0].send_keys("aaa")
        self.find(By.ID, "memberAdd_acctid")[0].send_keys("aaa")
        self.find(By.ID, "memberAdd_phone")[0].send_keys("13312345678")
        self.find(By.CSS_SELECTOR, "a.qui_btn.ww_btn.js_btn_save")[0].click()


if __name__ == '__main__':
    pass
