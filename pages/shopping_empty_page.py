from selenium.webdriver.common.by import By

from pages.base_page import Page


class ShoppingEmpty(Page):
    FOUND_TEXT = (By.XPATH, "//div[@class='a-row sc-your-amazon-cart-is-empty']")

    def verify_cart_empty(self, see_text):
        self.verify_result_text(see_text, *self.FOUND_TEXT)