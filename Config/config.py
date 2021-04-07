class TestData - empty:
    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager

    browser = webdriver.Chrome(ChromeDriverManager().install())

    base_url = browser.get('https://the-internet.herokuapp.com')
    checkPage_title = "Checkboxes"
