class TestData:

    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager

    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.implicitly_wait(10)

    base_url = browser.get('https://the-internet.herokuapp.com')

    url = browser.find_element_by_xpath('//a[text()="Checkboxes"]').click()
    checkbox_locator = browser.find_element_by_xpath('//input[@type="checkbox"][2]').click()
    checkPage_title = "Checkboxes"
