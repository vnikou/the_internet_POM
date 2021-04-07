from Pages.CheckboxPage import CheckboxPage
from Tests.conftest import TestData
from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage
from selenium import webdriver


def test_checkbox(browser):
    page = CheckboxPage(browser)
    page.load()
    page.maximize()


# Find the selected checkbox and select the one that is not selected
        ##i = 1
        for i in page.checkboxes:
            if page.checkbox_selected(i):
                print("The checkbox", i, " is selected!")
            else:
                page.click_checkbox(i)

        assert page.checkbox_selected(i)
        i += 1

    def get_checkbox_page_title(self):
        webdriver.CheckboxPage = CheckboxPage(self.driver)
        title = webdriver.CheckboxPage.get_checkbox_page_title(TestData.checkPage_title)
        assert title == TestData.checkPage_title
