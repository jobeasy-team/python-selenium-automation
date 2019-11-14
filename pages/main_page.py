from pages.base_page import Page
from selenium.webdriver.common.by import By


class MainPage(Page):
    SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
    SEARCH_ICON = (By.CSS_SELECTOR, "input.nav-input[type='submit']")
    ORDERS_LINK = (By.CSS_SELECTOR, "a#nav-orders span.nav-line-2")
    SHOPPING_CART = (By.ID, 'nav-cart-count')
    HAM_MENU = (By.ID, 'nav-hamburger-menu')

    def search_for_keyword(self, text):
        self.input_text(text, *self.SEARCH_INPUT)
        self.click(*self.SEARCH_ICON)

    def click_orders_link(self):
        self.click(*self.ORDERS_LINK)

    def click_cart(self):
        self.click(*self.SHOPPING_CART)

    def click_ham_menu(self):
        self.click(*self.HAM_MENU)

    def click_shopping_cart(self):
        self.click(*self.SHOPPING_CART)
