from selenium.webdriver.common.by import By

class CheckboxPage:

    url = 'https://the-internet.herokuapp.com/checkboxes'

    def __init__(self, driver):
        self.driver = driver


    def load(self):
        self.driver.get(self.url)

    def get_checkbox_page_title(self, title):
        return self.get_title(title)

    def maximize(self):
        self.driver.maximize_window()

    def checkboxes(self):
        return self.driver.find_elements(*self.checkboxes_locator)

    def number_checkboxes(self):
        checkboxes_number = len(self.driver.find_elements(*self.checkboxes_locator))
        return checkboxes_number

    def checkbox_selected(self, number):
        checkboxes = self.driver.find_elements(*self.checkboxes_locator)
        return checkboxes[number].is_selected()

    def click_checkbox(self, number):
        checkboxes = self.driver.find_elements(*self.checkboxes_locator)
        checkboxes[number].click()
