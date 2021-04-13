# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     mock_xiuqiu
   Description :
   Author :       mi
   date：          2021/4/12
-------------------------------------------------
   Change Activity:
                   2021/4/12:
-------------------------------------------------
"""
__author__ = 'mi'

import json
from mitmproxy import http, ctx


class Rewrite:
    def __init__(self):
        pass

    def response(self, flow: http.HTTPFlow):
        if "/batch/quote.json" in flow.request.pretty_url and "x=" in flow.request.pretty_url:
            """
            对一个股票维持原样；
            对第二个股票名字加长一倍；
            对第三个股票名字变成空"""
            content = json.loads(flow.response.content)
            content['data']['items'][1]['quote']['name'] = content['data']['items'][1]['quote']['name'] * 2
            content['data']['items'][2]['quote']['name'] = ''
            flow.response.text = json.dumps(content)


addons = [
    Rewrite()
]


