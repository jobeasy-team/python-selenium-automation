from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from support.logger import logger


class Page:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout=10)

    def open_url(self, end_url=''):
        url = f'https://www.target.com/{end_url}'
        logger.info(f'Opening page {url}')
        self.driver.get(url)

    def get_current_url(self):
        return self.driver.current_url

    def find_element(self, *locator):
        # logger.info(f'Searching for element by {locator}')
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        # logger.info(f'Searching for elements by {locator}')
        return self.driver.find_elements(*locator)

    def click(self, *locator):
        # logger.info(f'Clicking on element by {locator}')
        self.driver.find_element(*locator).click()

    def input_text(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def hover_element(self, *locator):
        element = self.find_element(*locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    def get_current_window(self):
        return self.driver.current_window_handle

    def switch_to_new_window(self):
        self.wait.until(EC.new_window_is_opened)
        all_windows = self.driver.window_handles
        print('All windows before switching:', all_windows)
        self.driver.switch_to.window(all_windows[1])
        print('Window after switch', self.get_current_window())

    def switch_to_window_by_id(self, window_id):
        self.driver.switch_to.window(window_id)
        print('Window after switch', self.get_current_window())

    def refresh_page(self):
        self.driver.refresh()

    def close(self):
        self.driver.close()

    def wait_until_clickable(self, *locator):
        element = self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f'Element by {locator} not clickable'
        )
        return element

    def wait_until_clickable_click(self, *locator):
        self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f'Element by {locator} not clickable'
        ).click()

    def wait_until_appear(self, *locator):
        element = self.wait.until(
            EC.visibility_of_element_located(locator),
            message=f'Element by {locator} not visible'
        )
        return element

    def wait_until_disappear(self, *locator):
        self.wait.until(
            EC.invisibility_of_element_located(locator),
            message=f'Element by {locator} still visible on the page'
        )

    def wait_until_url_contains(self, expected_partial_url):
        self.wait.until(
            EC.url_contains(expected_partial_url),
            message=f'Expected "{expected_partial_url}" not in "{self.driver.current_url}"'
        )

    def wait_until_url_to_be(self, expected_url):
        self.wait.until(
            EC.url_to_be(expected_url),
            message=f'Expected "{expected_url}", but got "{self.driver.current_url}"'
        )

    def verify_text(self, expected_text, *locator):
        actual_text = self.find_element(*locator).text
        assert actual_text == expected_text, \
            f'Expected "{expected_text}", but got "{actual_text}"'

    def verify_partial_text(self, expected_partial_text, *locator):
        actual_text = self.find_element(*locator).text
        assert expected_partial_text in actual_text, \
            f'Expected "{expected_partial_text}" not in "{actual_text}"'
