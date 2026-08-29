from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException

from support.logger import logger

class Page:
    OVERLAY = (By.CSS_SELECTOR, "[class*='styles_overlay']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout=10)
        self.base_url = 'https://www.target.com/'

    def open_url(self, end_url=''):
        url = f'{self.base_url}{end_url}'
        logger.info(f'Opening page: {url}')
        self.driver.get(url)
        self.dismiss_overlay()

    def dismiss_overlay(self):
        overlays = self.driver.find_elements(*self.OVERLAY)
        if not overlays:
            return

        logger.info('Overlay detected, attempting to dismiss')
        self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.ESCAPE)

        try:
            WebDriverWait(self.driver, 2).until(
                EC.invisibility_of_element_located(self.OVERLAY)
            )
            return
        except Exception:
            pass

        self.driver.execute_script(
            'document.querySelectorAll("[class*=\\"styles_overlay\\"]").forEach(el => el.remove());'
        )
        logger.info('Removed overlay via JavaScript')

    def find_element(self, *locator):
        logger.info(f'Searching for element by {locator}')
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        logger.info(f'Searching for elements by {locator}')
        return self.driver.find_elements(*locator)

    def click(self, *locator):
        logger.info(f'Clicking on element by {locator}')
        try:
            self.driver.find_element(*locator).click()
        except ElementClickInterceptedException:
            self.dismiss_overlay()
            self.wait_element_clickable_click(*locator)

    def input_text(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def get_element_text(self, *locator):
        return self.driver.find_element(*locator).text

    def get_current_window_handle(self):
        current_window = self.driver.current_window_handle
        # print('Current window', current_window)
        logger.info(f'Current window: {current_window}')
        return current_window

    def switch_to_new_window(self):
        self.driver.wait.until(EC.new_window_is_opened)
        print('All windows before switching', self.driver.window_handles)
        new_window = self.driver.window_handles[1]
        print('Switching to window', new_window)
        self.driver.switch_to.window(new_window)

    def switch_to_window_by_window_id(self, window_id):
        print('Switching to window', window_id)
        self.driver.switch_to.window(window_id)

    def close(self):
        self.driver.close()

    def wait_element_visible(self, *locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator),
            message=f'Element by {locator} not visible'
        )

    def wait_element_invisible(self, *locator):
        return self.wait.until(
            EC.invisibility_of_element_located(locator),
            message=f'Element by {locator} should be invisible'
        )

    def wait_element_clickable(self, *locator):
        return self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f'Element by {locator} not clickable'
        )

    def wait_element_clickable_click(self, *locator):
        self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f'Element by {locator} not clickable'
        ).click()

    def verify_element_text(self, expected_text, *locator):
        actual_text = self.get_element_text(*locator)
        assert expected_text == actual_text, \
            f'Expected {expected_text}, but got {actual_text}'

    def verify_partial_element_text(self, expected_partial_text, *locator):
        actual_text = self.get_element_text(*locator)
        assert expected_partial_text in actual_text, \
            f'Expected {expected_partial_text} not in {actual_text}'

    def verify_url(self, expected_url):
        actual_url = self.driver.current_url
        assert expected_url == actual_url, \
            f'Expected {expected_url}, but got {actual_url}'

    def verify_partial_url(self, expected_partial_url):
        actual_url = self.driver.current_url
        assert expected_partial_url in actual_url, \
            f'Expected {expected_partial_url} not in {actual_url}'