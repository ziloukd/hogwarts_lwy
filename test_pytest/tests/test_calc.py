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
        [-1, -1, 1],
        [1, -1, -1],
        [0, 0, 0],
        [2, 0, 0],
        [1, 1/3, 1/3],
        [1, -1/3, -1/3],
        [1/3, 1/3, 1/9],
        [-1/3, 1/3, -1/9],
        [2, 0.5, 1],
        [0.5, 0.5, 0.25],
    ])
    def test_mul(self, a, b, c):
        assert self.calc.mul(a, b) == c

    #正常场景
    @pytest.mark.parametrize('a, b, c', [
        [1, 2, 0.5],
        [1, 3, 1/3],
        [3, 2, 1.5],
        [0, 3, 0],
        [1/3, 3, 1/9],
        [5, -2, -2.5],
        [-5, -2, 2.5],
        [0.6, 0.2, 3],
    ])
    def test_div(self, a, b, c):
        assert self.calc.div(a, b) == c

    # 异常场景
    @pytest.mark.parametrize('a, b', [
        [0, 0],
        [2, 0],
        [0.2, 0],
        [-3, 0],
        [-0.2, 0],
    ])
    def test_div(self, a, b):
        with pytest.raises(ZeroDivisionError):
            self.calc.div(a, b)