# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test_calc
   Description :
   Author :       mi
   date：          2020/12/18
-------------------------------------------------
   Change Activity:
                   2020/12/18:
-------------------------------------------------
"""
__author__ = 'mi'

import pytest

from test_pytest.core.calc import Calc


class TestCalc:

    def setup_class(self):
        self.calc = Calc()

    @pytest.mark.parametrize('a, b, c', [
        [1, 2, 2],
        []
        [-1, -1, 1],
        [1, -1, 1]
    ])
    def test_mul(self, a, b, c):
        assert self.calc.mul(a, b) == c
        # assert calc.mul(-1, -1) == 1
        # assert calc.mul(1, -1) == 1
