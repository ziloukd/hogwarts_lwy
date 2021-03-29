# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     add_member_test
   Description :
   Author :       mi
   date：          2021/3/29
-------------------------------------------------
   Change Activity:
                   2021/3/29:
-------------------------------------------------
"""
__author__ = 'mi'

from assertpy import assert_that

from homework_app1.page.app import App


class TestAddMember:
    def setup(self):
        self.main = App()

    def teardown(self):
        pass

    def test_add_member(self):
        # 添加联系人
        result = self.main.start().main().goto_contact().goto_add_member().add_member()

        # 添加断言
        assert_that(result).is_equal_to('添加成功')
