from selenium.webdriver.common.by import By
from selenium import webdriver


class CheckboxPage:
    base_url = 'https://the-internet.herokuapp.com'

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.url)

    def maximize(self):
        self.driver.maximize_window(self)

    def checkbox_selected(self):
        checkbox = self.driver.find_elements(*self.checkbox_locator)
        return checkbox.is_selected()

    def click_checkbox(self, number):
        checkboxes = self.driver.find_elements(*self.checkboxes_locator)
        checkboxes[number].click()

    def get_checkbox_page_title(self, title):
        return self.get_title(title)
