# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     contacts_test
   Description :
   Author :       mi
   date：          2021/3/10
-------------------------------------------------
   Change Activity:
                   2021/3/10:
-------------------------------------------------
"""
__author__ = 'mi'

from homework_selenium2.page.index_page import IndexPage


class TestContacts():
    def setup(self):
        self.main = IndexPage()

    def test_delete_member(self):
        # 1.进入通讯录页面
        step = self.main.goto_login().login_by_cookies().switch_item("contacts")
        # 2.执行删除操作
        step.delete_member("张三39")
        # 3.检测是否删除成功
        assert step.find_member("张三39") == False
