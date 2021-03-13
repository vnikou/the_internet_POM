from Pages.Checkbox import CheckboxPage
import pytest
from Config.config import TestData
from selenium.webdriver.common.by import By


class Test_Checkbox():

    def test_Checkbox(self):
        page = CheckboxPage(self)
        page.load()
        page.maximize()

    def get_checkbox_page_title(self):
        self.checkboxpage = Checkbox(self.driver)
        title = self.checkboxpage.get_checkbox_page_title(TestData.checkpage_title)
        assert title == TestData.input_title

    def get_page_title(self):
        self.checkbox = Checkbox(self, driver)
        self.checkbox.get.title(TestData.checkpage_title)



        checkbox2 = driver.find_element (By.XPATH,'//input[@type="checkbox"][2]')
        if checkbox2.is_selected() == False:
            checkbox2.click()

        checkbox1 = (By.XPATH, '//input[@type="checkbox"][1]')

        if checkbox1.is_selected() == False:
            checkbox1.click()

            assert checkbox1.get_attribute('checked')
