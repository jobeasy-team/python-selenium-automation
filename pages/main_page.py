from pages.base_page import Page
from selenium.webdriver.common.by import By


class MainPage(Page):
    ORDER = (By.CSS_SELECTOR, "a[href='/gp/css/order-history?ref_=nav_orders_first']")
    CART = (By.ID, "nav-cart")

    def open(self):
        self.open_page()

    def click_order(self):
        self.click(*self.ORDER)

    def click_cart(self):
        self.click(*self.CART)


