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
import pytest
from assertpy import assert_that

from framwork_api1.tag import Tag


class TestAddTag:

    def setup(self):
        self._main = Tag()
        self._main.get_token()

        # 初始化标签
        # 删除所有标签
        tag_list = self._main.tag_get_list()
        for tag_info in tag_list:
            self._main.tag_delete(tag_info["tagid"])
        # 添加一个重复标签
        self._main.tag_add("tag2")

    def teardown(self):
        # 删除所有标签
        tag_list = self._main.tag_get_list()
        for tag_info in tag_list:
            self._main.tag_delete(tag_info["tagid"])

    @pytest.mark.parametrize("title,tag_name,expect",
                             [
                                 ("传参正常添加成功", "tag汉", 0),
                                 ("添加重复标签失败", "tag2", 40071),
                                 ("添加空标签失败", "", 40072),
                                 ("添加标签长度为31,成功", "a"*31, 0),
                                 ("添加标签长度为32，成功", "a"*32, 0),
                                 ("添加标签长度为33，失败", "a"*33, 40058),
                                 ("添加非数字汉字字母，失败", "，", 444),

                              ])
    def test_add_tag(self, title, tag_name, expect):
        # 创建标签
        print(title)
        res = self._main.tag_add(tag_name)
        assert_that(res["errcode"]).is_equal_to(expect)

