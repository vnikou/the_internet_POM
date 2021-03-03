from Config.config import TestData
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest

class Test_Login(BaseTest):

assert "The Internet" in browser.title

img = browser.find_element_by_xpath('//a[text()="Broken Images"]').click()
images = browser.find_elements_by_css_selector("img")

for image in images:
    print(image.get_attribute("src"))
    findimg = requests.get(image.get_attribute("src"))
    print(findimg.status_code)
    if findimg.status_code != 200:
        print(image.get_attribute("src"), "The image is broken!")

browser.back()
