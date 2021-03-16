import pytest
from Pages.Inputs import Inputs
from Config.config import TestData
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Pages.BasePage import BasePage


class TestInputs(BasePage):

    def test_inputs(self):
        page = Inputs(self)
        page.load()
        page.maximize()

    def get_input_page_title(self):
        self.inputpage = input(self.driver)
        title = self.inputpage.get_input_page_title(TestData.input_title)
        assert title == TestData.input_title

    inputs1 = (By.XPATH, '//a[text()="Inputs"]')
    inputs2 = (By.XPATH, '//input')
    inputs2.send_Keys('123456789')

    assert inputs2.get_attribute('value') == '123456789'
