class TestData:
    base_url = 'https://the-internet.herokuapp.com'

    checkpage_title = "Broken Images"
    input_title = "Inputs"

    def open_site(base_url):
        import pytest
        from selenium import webdriver
        driver = webdriver.Chrome(executable_path="C:\webdrivers\chromedriver.exe")
