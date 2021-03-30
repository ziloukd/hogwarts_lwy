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
        self._start = self.main.start().main()

    def teardown(self):
        pass

    def test_add_member(self):
        # 添加联系人
        result = self.main.start().main().goto_contact().goto_add_member().add_member()

        # 添加断言
        assert_that(result).is_equal_to('添加成功')

    def test_delete_member(self):
        res = self._start.goto_contact().goto_enterprise_contact().goto_contact_edit().delete_member().verify_delete()
        assert_that("添加成功").is_equal_to("添加成功")