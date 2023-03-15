from selenium.webdriver.common.by import By
from pages.base_page import Page


class ProductPage(Page):
    ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')


    def click_add_to_cart(self):
        self.wait_for_element_click(*self.ADD_TO_CART_BTN)
