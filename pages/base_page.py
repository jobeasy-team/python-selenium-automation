from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Support.logger import logger


class Page:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.base_url = 'https://www.amazon.com'

    def click(self, *locator):
        logger.info(f'Clicking on {locator}')
        self.driver.find_element(*locator).click()

    def open_page(self, end_url=''):
        logger.info(f'{self.base_url}{end_url}')
        self.driver.get(f'{self.base_url}{end_url}')

    def input_text(self, text, *locator):
        e = self.driver.find_element(*locator)
        e.clear()
        logger.info(f'Inputting {text}')
        e.send_keys(text)

    def verify_partial_text(self, expected_text, *locator):
        actual_text = self.driver.find_element(*locator).text
        assert expected_text in actual_text, \
            f'Expected text {expected_text} is not in {actual_text}'

    def verify_url_contains_query(self, query):
        assert query in self.driver.current_url, f'{query} not in {self.driver.current_url}'

    def verify_text(self, exp_txt, *locator):
        act_txt = self.driver.find_element(*locator).text

        assert exp_txt == act_txt, \
            f'Error,{act_txt} does not match {exp_txt}'

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(locator)

    def wait_for_element_disappear(self, *locator):
        self.wait.until(EC.invisibility_of_element(locator))

    def wait_for_element_click(self, *locator):
        e = self.wait.until(EC.element_to_be_clickable(*locator))
        e.click()

    def wait_for_element_appear(self, *locator):
        return self.wait.until(EC.presence_of_element_located(locator))
