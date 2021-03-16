from Pages.Checkbox import CheckboxPage
import pytest
from Config.config import TestData
from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


def test_checkbox(browser):
        page = CheckboxPage(browser)
        page.load()
        page.maximize()


def get_checkbox_page_title(browser):
        browser.checkboxpage = CheckboxPage(browser.driver)
        title = browser.checkboxpage.get_checkbox_page_title(TestData.checkpage_title)
        assert title == TestData.checkpage_title

# Find the selected checkbox
        box1 = (By.XPATH, '//input[@type="checkbox"][1]')
        if box1.is_selected():
            print("box1 is selected")
        else:
            print("box1 is not selected")

        box2 = (By.XPATH, '//input[@type="checkbox"][2]')
        if box2.is_selected():
            print("box2 is selected")
        else:
            print("box2 is not selected")

        if not box1.is_selected():
            box1.click()

        if not box2.is_selected():
            box2.click()

            assert box1.get_attribute('checked')
