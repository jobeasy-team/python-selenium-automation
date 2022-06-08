from selenium.webdriver.common.by import By

from pages.base_page import Page


# represents the header on Amazon page that can be found on all pages
# methods specificly for header

class Header(Page):
    SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
    SEARCH_BTN = (By.ID, 'nav-search-submit-button')
    cart_icon = (By.CSS_SELECTOR, 'div#nav-cart-count-container span.nav-cart-count.nav-cart-0')
    ord_btn = (By.CSS_SELECTOR, 'a[href*="order-history"]')

    def search_amazon(self, search_word):
        self.input_text(search_word, *self.SEARCH_INPUT)  # use self to ref class.
        self.click(*self.SEARCH_BTN)

    def orders_btn(self):
        self.click(*self.ord_btn)

    def cart_btn(self):
        self.click(*self.cart_icon)
