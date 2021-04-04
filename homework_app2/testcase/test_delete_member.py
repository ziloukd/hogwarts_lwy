# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test_delete_member
   Description :
   Author :       lwy
   date：          2021/4/4
-------------------------------------------------
   Change Activity:
                   2021/4/4:
-------------------------------------------------
"""
__author__ = 'lwy'

from assertpy import assert_that

from homework_app2.page.app import App


class TestAddMember:
    def setup(self):
        self._app = App()
        self._main = self._app.start().main()

    def test_delete_member(self):
        # 1.进入编辑页
        step1 = self._main.goto_contact().goto_enterprise_contact().goto_contact_edit()
        # 2.删除成员
        step2 = step1.delete_member()
        # 3.验证结果
        result = step2.verity_delete_member()
        assert_that('删除成功').is_equal_to(result)
