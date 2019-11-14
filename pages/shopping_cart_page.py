from pages.base_page import Page
from selenium.webdriver.common.by import By


class ShoppingCart(Page):
    SHOP_CART = (By.ID, "sc-retail-cart-container")

    def verify_cart_empty(self, expected_text):
        self.verify_text(expected_text, *self.SHOP_CART)


