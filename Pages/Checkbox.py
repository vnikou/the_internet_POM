from selenium.webdriver.common.by import By


class CheckboxPage:

    url = 'https://the-internet.herokuapp.com/checkboxes'

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.url)

    def maximize(self):
        self.driver.maximize_window()

    def get_checkbox_page_title(self, title):
        return self.get_title(title)

    def checkbox_selected(self, number):
        checkbox = self.driver.find_elements(self.checkbox)
        return checkbox.is_selected()
