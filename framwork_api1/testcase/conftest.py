# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     conftest
   Description :
   Author :       mi
   date：          2021/4/21
-------------------------------------------------
   Change Activity:
                   2021/4/21:
-------------------------------------------------
"""
__author__ = 'mi'

def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: list["Item"]
) -> None:
    # item表示每个测试用例，解决用例名称中文显示问题
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode-escape")
        item._nodeid = item._nodeid.encode("utf-8").decode("unicode-escape")
