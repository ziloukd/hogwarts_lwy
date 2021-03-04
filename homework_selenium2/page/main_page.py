# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     main
   Description :
   Author :       mi
   date：          2021/3/2
-------------------------------------------------
   Change Activity:
                   2021/3/2:
-------------------------------------------------
"""
__author__ = 'mi'

from selenium.webdriver.common.by import By

from homework_selenium2.page.app_management_page import AppManagementPage
from homework_selenium2.page.base_page import BasePage
from homework_selenium2.page.contacts_page import ContactsPage
from homework_selenium2.page.customer_contacts_page import CustomerContactsPage
from homework_selenium2.page.home_page import HomePage
from homework_selenium2.page.management_tools_page import ManagementToolsPage
from homework_selenium2.page.my_company_page import MyCompanyPage


class MainPage(BasePage):
    def switch_item(self, item: str):
        items = self.finds(By.CSS_SELECTOR, ".frame_nav_item_title")

        # 切换页面
        if item == "home_page":
            items[0].click()
            return HomePage(self._driver)
        elif item == "contacts":
            items[1].click()
            return ContactsPage(self._driver)
        elif item == "app_management":
            items[2].click()
            return AppManagementPage(self._driver)
        elif item == "customer_contacts":
            items[3].click()
            return CustomerContactsPage(self._driver)
        elif item == "management_tools":
            items[4].click()
            return ManagementToolsPage(self._driver)
        elif item == "my_company":
            items[5].click()
            return MyCompanyPage(self._driver)
