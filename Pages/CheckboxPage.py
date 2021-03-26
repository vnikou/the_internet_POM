from selenium.webdriver.common.by import By
from Config.config import TestData
from Pages.BasePage import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckboxPage(BasePage):

    url = 'https://the-internet.herokuapp.com/checkboxes'

    checkboxes = (By.XPATH, "//input[@type='checkbox']")

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.url)

    def maximize(self):
        self.driver.maximize_window()

    def checkbox_selected(self, number):
        checkbox = self.driver.find_elements(self.checkboxes)
        return checkbox.is_selected()

    def click_checkbox(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def get_checkbox_page_title(self, title):
        return self.get_title(title)
