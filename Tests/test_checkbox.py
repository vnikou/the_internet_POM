from Pages.Checkbox import CheckboxPage
import pytest
from Config.config import TestData
from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


def test_checkbox(browser):
        page = CheckboxPage(browser)
        page.load()
        page.maximize()


# Find the selected checkbox and select the one that is not selected
        i = 1
        for i in page.checkboxes:
            if page.checkbox_selected(i):
                print("The checkbox", i, " is selected!")
            else:
                page.click_checkbox(i)

        assert page.checkbox_selected(i)
        i += 1


def get_checkbox_page_title(browser):
        browser.checkboxpage = CheckboxPage(browser.driver)
        title = browser.checkboxpage.get_checkbox_page_title(TestData.checkpage_title)
        assert title == TestData.checkpage_title
