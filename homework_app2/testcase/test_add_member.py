# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test_add_member
   Description :
   Author :       mi
   date：          2021/4/1
-------------------------------------------------
   Change Activity:
                   2021/4/1:
-------------------------------------------------
"""
__author__ = 'mi'

from assertpy import assert_that

from homework_app2.page.app import App


class TestAddMember:
    def setup(self):
        self._app = App()
        self._main = self._app.start().main()

    def test_add_member(self):
        # 1.进入编辑页
        step1 = self._main.goto_contact().goto_member_invite_menu().goto_contact_add()
        # 2.录入信息
        step2 = step1.add_member()
        # 3.验证
        # res = step2.verity_toast()
        # assert_that(res).is_equal_to('添加成功')
        print(step2._driver.page_source)