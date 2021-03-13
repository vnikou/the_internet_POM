import pytest
from Config.config import TestData
from Pages.Broken_image import BrokenImage
from selenium.webdriver.common.by import By
import requests

class Test_BrokenImage():

    def test_broken_image(self):
        page = BrokenImage(driver)
        page.load()
        page.maximize()

    def get_page_title(self):
        self.checkbox = Checkbox(self, driver)
        self.checkbox.get.title(TestData.checkpage_title)
        title = broken_image.get_page_title

        broken.get_page_title(BrokenImage.PAGE_TITLE)

    images = (By.CSS_SELECTOR, "img")

    for image in images:

            print(image.get_attribute("src"))
            findimg = requests.get(image.get_attribute("src"))
            print(findimg.status_code)
    if findimg.status_code != 200:
            print(image.get_attribute("src"), "The image is broken!")
