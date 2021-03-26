# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     base_page
   Description :
   Author :       mi
   date：          2021/3/22
-------------------------------------------------
   Change Activity:
                   2021/3/22:
-------------------------------------------------
"""
__author__ = 'mi'

import yaml
from appium.webdriver.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver = None):
        self._params = {}
        self._black_list = []
        self._error_count = 10
        self._driver = driver

    def find(self, by, locator=None):
        try:
            elements = self._driver.find_elements(*by) if isinstance(by, tuple) else self._driver.find_elements(by, locator)
            self._error_count = 0
            return elements[0]
        except Exception as e:
            self._error_count += 1
            if self._error_count < 10:
                for black in self._black_list:
                    elements: list = self._driver.find_elements(*black)
                    if len(elements) != 0:
                        elements[0].click()
            else:
                raise e

    def steps(self, filepath):
        with open(filepath, "r", encoding="utf-8") as f1:
            steps: list[dict] = yaml.safe_load(f1)
            for step in steps:
                if "by" in step.keys():
                    element = self.find(step["by"], step["locator"])
                if "action" in step.keys():
                    if step["action"] == "click":
                        element.click()
                    if step["action"] == "send":
                        content: str = step["value"]
                        for param in self._params:
                            content = content.replace("%s" % param, self._params[param])
                            element.send_keys(content)


if __name__ == '__main__':
    test = BasePage()
    test.steps("../page/test.yaml")