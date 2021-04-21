# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     tag.py
   Description :
   Author :       mi
   date：          2021/4/19
-------------------------------------------------
   Change Activity:
                   2021/4/19:
-------------------------------------------------
"""
__author__ = 'mi'

import requests


class Tag:

    def __init__(self):
        self._token = ""
        self._corpid = "ww4523badabe77c4bc"
        self._corpsecret = "YjtZCbMNJRxzk4G-NnSlW1dmk03d7wNia8cZWHyFTvY"

    def get_token(self):
        """获取token，保存token为类属性"""
        params = {
            "corpid": self._corpid,
            "corpsecret": self._corpsecret,
        }
        res  = requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken", params=params)
        self._token = res.json()["access_token"]
        return

    def tag_add(self, tag_name):
        """添加标签，返回response"""
        params = {
            "access_token": self._token
        }
        body = {
            "tagname": tag_name,
        }
        res = requests.post("https://qyapi.weixin.qq.com/cgi-bin/tag/create", params=params, json=body)
        return res.json()

    def tag_get_list(self):
        """获取，标签列表"""
        params = {
            "access_token": self._token
        }
        res = requests.get("https://qyapi.weixin.qq.com/cgi-bin/tag/list", params=params)
        # tag_list = [i["tagname"] for i in res.json()["taglist"]]
        return res.json()["taglist"]

    def tag_delete(self, tagid):
        """删除标签"""
        params = {
            "access_token": self._token,
            "tagid": tagid
        }
        res = requests.get("https://qyapi.weixin.qq.com/cgi-bin/tag/delete", params=params)
        return res.json()



if __name__ == '__main__':
    test = Tag()
    test.get_token()
    print(test.tag_get_list())
    # test.tag_delete(1)