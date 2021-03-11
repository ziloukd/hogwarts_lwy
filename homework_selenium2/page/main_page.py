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


from homework_selenium2.page.base_page import BasePage


class MainPage(BasePage):
    def switch_item(self, item: str):
        items = self.finds(By.CSS_SELECTOR, ".frame_nav_item_title")

        # 切换页面
        if item == "home_page":
            items[0].click()
            from homework_selenium2.page.home_page import HomePage
            return HomePage(self._driver)
        elif item == "contacts":
            items[1].click()
            from homework_selenium2.page.contacts_page import ContactsPage
            return ContactsPage(self._driver)
        elif item == "app_management":
            items[2].click()
            from homework_selenium2.page.app_management_page import AppManagementPage
            return AppManagementPage(self._driver)
        elif item == "customer_contacts":
            items[3].click()
            from homework_selenium2.page.customer_contacts_page import CustomerContactsPage
            return CustomerContactsPage(self._driver)
        elif item == "management_tools":
            items[4].click()
            from homework_selenium2.page.management_tools_page import ManagementToolsPage
            return ManagementToolsPage(self._driver)
        elif item == "my_company":
            items[5].click()
            from homework_selenium2.page.my_company_page import MyCompanyPage
            return MyCompanyPage(self._driver)
