# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     base_page
   Description :
   Author :       mi
   date：          2021/3/31
-------------------------------------------------
   Change Activity:
                   2021/3/31:
-------------------------------------------------
"""
__author__ = 'mi'

import yaml
from appium.webdriver.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver = None):
        self._driver = driver
        self._error_num = 0
        self._black_list = {}

    def find(self, by, locator):
        try:
            elements = self._driver.find_elements(*by) if isinstance(by, tuple) else self._driver.find_elements(by,
                                                                                                                locator)
            return elements[0]
        except Exception as e:
            self._error_num += 1
            if self._error_num < 10:
                for black in self._black_list:
                    elements = self._driver.find_elements(*self._black_list[black])
                    if len(elements) > 0:
                        elements[0].click()
                return self.find(by, locator)
            else:
                raise e

    def find_by_scroll(self, text: str):
        return self.find('-android uiautomator', 'new UiScrollable(new UiSelector()'
                                                 '.scrollable(true).instance(0)).'
                                                 'scrollIntoView(new UiSelector().'
                                                 f'text("{text}").instance(0));')

    def steps(self, filename):
        with open(filename, 'r', encoding='utf-8') as f1:
            steps: list[dict] = yaml.safe_load(f1)
            for step in steps:
                if 'by' in step.keys():
                    element = self.find(step['by'], step['locator'])
                if 'action' in step.keys():
                    if step['action'] == 'click':
                        element.click()
                    elif step['action'] == 'send':
                        element.send_keys(step['value'])

    def get_toast_text(self):
        elements = self._driver.find_elements('xpath', '//*[@class="android.widget.Toast"]')
        if len(elements) > 0:
            return elements[0].text
        else:
            return None
