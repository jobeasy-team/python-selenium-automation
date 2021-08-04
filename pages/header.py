from pages.base_page import Page
from selenium.webdriver.common.by import By

class Header(Page):
    SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
    SEARCH_ICON = (By.ID, 'nav-search-submit-button')
    CART_ICON = (By.ID, 'nav-cart')
    EMPTY_CART_MESSAGE = (By.ID, 'sc-empty-cart-message')
    ORDERS_LINK = (By.ID, "nav-orders")

    def input_search(self):
        self.input_text('Table', *self.SEARCH_FIELD)
        
    def click_search(self):
        self.click(*self.SEARCH_ICON)

    def click_cart(self):
        self.click(*self.CART_ICON)

    def click_orders(self):
        self.click(*self.ORDERS_LINK)

    def verify_empty_cart(self):
        self.driver.find_element(*self.EMPTY_CART_MESSAGE)
