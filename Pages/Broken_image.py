from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage

class BrokenImage():

    url = 'https://the-internet.herokuapp.com/broken_images'
    PAGE_TITLE = "BROKEN IMAGE"

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.url)

    def maximize(self):
        self.driver.maximize_window()

    def get_page_title(self):
        return self.get_page_title()
