class TestData:
    base_url = 'https://the-internet.herokuapp.com'
    driver = webdriver.Chrome(ChromeDriverManager().install())
    browser = webdriver.Chrome()
    browser.get(base_url)
