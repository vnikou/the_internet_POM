import pytest
from selenium import webdriver


@pytest.fixture(params=["Chrome"], scope='class')
def init_driver(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome(executable_path="C:/webdrivers/chromedriver.exe")
    request.cls.driver = web_driver
    yield
    web_driver.close()
