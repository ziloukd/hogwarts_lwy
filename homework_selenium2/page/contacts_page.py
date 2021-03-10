from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from homework_selenium2.page.base_page import BasePage


class ContactsPage(BasePage):
    def delete_member(self, name: str):
        # 判断name是否在通讯名单内,如果在，则中复选框，点击删除
        res = self.find_member(name)
        if res:
            self.find(By.XPATH, f"//td[@title='{name}']/../td[1]").click()
            self.find(By.CSS_SELECTOR, ".js_delete").click()
            self.find(By.CSS_SELECTOR, ".qui_btn[d_ck='submit']").click()

    def find_member(self, name: str):
        # 显示等待
        locator = (By.CSS_SELECTOR, ".js_checkbox_container")
        self.wait().until(expected_conditions.element_to_be_clickable(locator))

        # 获取页面数
        try:
            page_num = self.find(By.CSS_SELECTOR, ".ww_pageNav_info_text")
            current_page, total_page = (int(i) for i in page_num.text.split("/"))
            count = total_page - current_page
        except NoSuchElementException:
            count = 1

        # 查询name是否在当前展示名单内
        for i in range(count):
            eles = self.finds(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
            member_list = [i.get_attribute("title") for i in eles]
            if name in member_list:
                return True
            try:
                self.find(By.CSS_SELECTOR, ".js_next_page").click()
            except NoSuchElementException:
                return False
        return False


if __name__ == '__main__':
    test = ContactsPage(debug=True)
    # test.delete_member("张三45")
    print(test.find_member("张三45"))