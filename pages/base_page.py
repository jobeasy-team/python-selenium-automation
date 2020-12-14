from selenium.webdriver.support.wait import WebDriverWait


class Page:

    def __init__(self, driver):
        self.driver = driver
        # BELOW LINE MOVED FROM AMAZON_SEARCH.PY
        self.driver.wait = WebDriverWait(self.driver, 15)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def open_page(self, url):
        self.driver.get(url)

    def input_text(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def verify_result_text(self, verify_text, *locator):
        result = self.driver.find_element(*locator)
        assert result.text == verify_text, f'Got Error. Expected {verify_text}, but got {result.text}'