from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Page:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://www.amazon.com/"
        self.wait = WebDriverWait(self.driver, 15)
        self.url = driver.current_url

    def click(self, *locator):
        """
        Clicks on WebElement
        :param locator: search strategy for find_element of a Web Element..
        """
        self.driver.find_element(*locator).click()

    def input_text(self, text, *locator):
        e = self.driver.find_element(*locator)
        e.clear()
        e.send_keys(text)

    def open_page(self, url=''):
        self.driver.get(self.base_url + url)

    def verify_text(self, expected_text, *locator):
        actual_text = self.driver.find_element(*locator).text
        assert expected_text in actual_text, f"Expected {expected_text}, but got {actual_text}"

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def wait_for_element_click(self, *locator):
        e = self.driver.wait.until(EC.element_to_be_clickable(locator))
        e.click()

    def wait_for_element_disappear(self, *locator):
        self.driver.wait.until(EC.invisibility_of_element(locator))

    def wait_for_element_appear(self, *locator):
        self.driver.wait.until(EC.presence_of_element_located(locator))

    def verify_url(self, url=''):
        self.url = self.driver.current_url
        assert url in self.url


