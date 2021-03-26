import pytest


class TestData:
    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager
    options = webdriver.ChromeOptions()

    browser = webdriver.Chrome(ChromeDriverManager().install())
    base_url = 'https://the-internet.herokuapp.com'
    browser.implicitly_wait(10)

    input_title = "Inputs"
    checkpage_title = "Checkboxes"

