from selenium.webdriver.common.by import By

from pages.base_page import Page


class Productpage(Page):
    one_time = (By.CSS_SELECTOR, 'div a i.a-icon.a-accordion-radio.a-icon-radio-inactive')
    add_to_cart_btn = (By.ID, 'add-to-cart-button')

    def add_to_cart(self):
        self.click(*self.one_time)
        self.click(*self.add_to_cart_btn)