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
import pytest

from homework_app2.page.app import App


class TestAddMember:
    def setup(self):
        self._app = App()
        self._main = self._app.start().main()

    def test_add_member(self):
        pass
        
