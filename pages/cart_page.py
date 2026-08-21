from selenium.webdriver.common.by import By

from pages.base_page import Page

class CartPage(Page):
    CART_EMPTY_MSG = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg'] h1")
    # Strings:
    cart_empty_txt = 'Your cart is empty'

    def open_cart(self):
        self.open_url(end_url='cart')

    def verify_empty_cart_msg(self):
        self.verify_element_text(self.cart_empty_txt, *self.CART_EMPTY_MSG)
