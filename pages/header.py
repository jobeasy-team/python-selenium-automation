from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from pages.base_page import Page


# represents the header on Amazon page that can be found on all pages
# methods specificly for header

class Header(Page):
    SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
    SEARCH_BTN = (By.ID, 'nav-search-submit-button')
    cart_icon = (By.CSS_SELECTOR, 'div#nav-cart-count-container span.nav-cart-count.nav-cart-0')
    ord_btn = (By.CSS_SELECTOR, 'a[href*="order-history"]')
    SEARCH_DROPDOWN = (By.CSS_SELECTOR, '#searchDropdownBox')
    DEPT_BOOKS = (By.CSS_SELECTOR, '[data-category= "books"]')
    NAV_APPAREL = (By.CSS_SELECTOR, '[data-category= "apparel"]')
    NEW_ARR = (By.CSS_SELECTOR, '[href*="New-Arrivals"]')
    WOMEN_DEALS = (By.CSS_SELECTOR, '[src*="W."]')

    def search_amazon(self, search_word):
        self.input_text(search_word, *self.SEARCH_INPUT)
        self.click(*self.SEARCH_BTN)

    def orders_btn(self):
        self.click(*self.ord_btn)

    def cart_btn(self):
        self.click(*self.cart_icon)

    def select_dept(self):
        dept_select = self.find_element(*self.SEARCH_DROPDOWN)
        select = Select(dept_select)
        select.select_by_value('search-alias=stripbooks')

    def verify_dept(self):
        # self.wait_for_element_appear(*self.DEPT_BOOKS)
        self.wait_for_element_appear(*self.NAV_APPAREL)

    def hover_sub_nav(self):
        actions = ActionChains(self.driver)
        new_arr = self.find_element(*self.NEW_ARR)
        actions.move_to_element(new_arr)
        actions.perform()

    def verify_deals(self):
        self.wait_for_element_appear(*self.WOMEN_DEALS)
