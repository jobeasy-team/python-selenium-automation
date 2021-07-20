from pages.base_page import Page
from selenium.webdriver.common.by import By

class Shopping_Cart(Page):
    Empty_cart = (By.CSS_SELECTOR, "h2.sc-your-amazon-cart-is-empty")

    def verify_empty_cart(self):
        actual_result = self.driver.find_element(*self.Empty_cart).text
        expected_result = 'Your Amazon Cart is empty'
        assert expected_result == actual_result, f'Expected {expected_result}, but got {actual_result}'


