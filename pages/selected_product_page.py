from selenium.webdriver.common.by import By
from pages.base_page import Page


class SelectedProductPage(Page):

    ADD_TO_CART = (By.ID, "add-to-cart-button")

    def click_add_to_cart(self):
        self.click(*self.ADD_TO_CART)