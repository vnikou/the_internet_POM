from Config.config import TestData
from Pages.BasePage import BasePage
from selenium import webdriver
driver = webdriver.Chrome()


class Inputs(BasePage):

    url = 'https://the-internet.herokuapp.com/inputs'

    def __init__(self, driver):
        super().__init__(self, driver)

    """Page actions"""
    def load(self):
        self.driver.get(self.url)

    def get_input_page_title(self, title):
        return self.get_title(title)

