from pages.base_page import Page
from selenium.webdriver.common.by import By


class CartPage(Page):
    EMPTY_CART_TEXT = (By.CSS_SELECTOR, 'div.sc-your-amazon-cart-is-empty h2')

    def verify_cart_text(self, expected_text):
        self.verify_text(expected_text, *self.EMPTY_CART_TEXT)
