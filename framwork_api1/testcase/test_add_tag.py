# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test_add_tag
   Description :
   Author :       mi
   date：          2021/4/19
-------------------------------------------------
   Change Activity:
                   2021/4/19:
-------------------------------------------------
"""
__author__ = 'mi'

from framwork_api1.tag import Tag
from assertpy import assert_that


class TestAddTag:

    def setup(self):
        self._main = Tag()
        self._main.get_token()

    def teardown(self):
        pass

    def test_add_tag(self):
        tag_name = "tag2"
        # 创建标签
        step1 = self._main.tag_add(tag_name)
        # 验证是否创建成功
        tag_list = self._main.tag_get_list()
        assert_that(tag_list).contains(tag_name)
