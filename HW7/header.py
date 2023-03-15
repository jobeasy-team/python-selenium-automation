from pages.base_page import Page
from selenium.webdriver.common.by import By


class Header(Page):
    AMAZON_SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
    SEARCH_ICON = (By.ID, 'nav-search-submit-button')
    RETURNS_ORDERS = (By.ID, 'nav-orders')
    CART_ICON = (By.ID, 'nav-cart')
    CART_COUNT = (By.ID, 'nav-cart-count')

    def input_search_text(self, text):
        self.input_text(text, *self.AMAZON_SEARCH_FIELD)

    def click_search(self):
        self.click(*self.SEARCH_ICON)

    def click_ReturnsAndOrders(self):
        self.wait_for_element_click(*self.RETURNS_ORDERS)


    def click_cart_icon(self):
        self.click(*self.CART_ICON)


    def verify_cart_count(self,expected_count):
        self.verify_text(expected_count, *self.CART_COUNT)