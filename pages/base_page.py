from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Page:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def input_text(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def wait_for_element_click(self, *locator):
        self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f'Element by {locator} not clickable'
        ).click()

    def wait_for_element(self, *locator):
        self.wait.until(
            EC.visibility_of_element_located(locator),
            message=f'Element by {locator} not visible'
        )

    def wait_for_element_disappear(self, *locator):
        self.wait.until(
            EC.invisibility_of_element_located(locator),
            message=f'Element by {locator} still visible'
        )

    def wait_for_url_contains(self, partial_url):
        self.wait.until(EC.url_contains(partial_url), message=f'Expected {partial_url} not in URL')

    def verify_text(self, expected_text, *locator):
        actual_text = self.driver.find_element(*locator).text
        assert expected_text == actual_text, f"Expected text '{expected_text}' did not match actual '{actual_text}'"

    def verify_partial_text(self, expected_partial_text, *locator):
        actual_text = self.driver.find_element(*locator).text
        assert expected_partial_text in actual_text, \
            f"Expected text '{expected_partial_text}' not in actual '{actual_text}'"

    def verify_url(self, expected_url):
        actual_url = self.driver.current_url
        print('Current URL: ', actual_url)
        assert expected_url == actual_url, \
            f"Expected URL {expected_url} did not match actual URL {actual_url}"

    def verify_partial_url(self, expected_partial_url):
        actual_url = self.driver.current_url
        print('Current URL: ', actual_url)
        assert expected_partial_url in actual_url, \
            f"Expected URL {expected_partial_url} in actual URL {actual_url}"

