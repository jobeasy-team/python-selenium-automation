from pages.base_page import Page
from selenium.webdriver.common.by import By


class MainPage(Page):
    SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
    SEARCH_ICON = (By.XPATH, "//input[@value='Go']")
    CART_ICON = (By.CSS_SELECTOR, "a[href='/gp/css/order-history?ref_=nav_orders_first']")
    BUTTON = (By.CSS_SELECTOR, "a[href='/gp/css/order-history?ref_=nav_orders_first']")

    def open_amazon(self):
        self.open_page('https://www.amazon.com/')

    # def click_search_icon(self):
    #    self.click(*self.SEARCH_ICON)

    # def click_returns_orders(self):
    #    self.click(*self.BUTTON)
        
    def click_item(self, *locator):
        self.click(*locator)

    def input_search_word(self, search_word):
        print("in main1" + search_word)
        # self.input_text(search_word *self.SEARCH_INPUT)
        # self.driver.input_text(*self.SEARCH_INPUT)
        self.input_text(search_word, *self.SEARCH_INPUT)

    def click_sign_in(self):
        self.click(*self.CART_ICON)

