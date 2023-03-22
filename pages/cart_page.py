from selenium.webdriver.common.by import By
from pages.base_page import Page


class CartPage(Page):
    VERIFYTEXT = (By.CSS_SELECTOR, "div.sc-cart-header")

    def verify_search_result(self, expected_result):
        actual_result = self.driver.find_element(*self.VERIFYTEXT).text
        assert expected_result == actual_result, f'Expected {expected_result} but got actual {actual_result}'