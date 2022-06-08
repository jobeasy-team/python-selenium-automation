from selenium.webdriver.common.by import By

from pages.base_page import Page


class Cart(Page):
    empty = (By.CSS_SELECTOR, 'div.a-row.sc-your-amazon-cart-is-empty h2')
    added_cart = (By.CSS_SELECTOR, 'span.a-size-medium-plus.a-color-base.sw-atc-text.a-text-bold')

    def cart_empty(self, exp_res):
        self.verify_text(exp_res, *self.empty)

    def cart_fill(self, exp_res):
        self.verify_text(exp_res, *self.added_cart)
