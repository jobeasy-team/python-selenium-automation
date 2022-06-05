from selenium.webdriver.common.by import By

from pages.base_page import Page


class Header(Page):
    SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
    SEARCH_BTN = (By.ID, 'nav-orders')
    LOCATOR   = (By.ID, 'nav-orders')

    def search_amazon(self, search_word):
        self.input_text(search_word, *self.SEARCH_INPUT)
        self.click(*self.SEARCH_BTN)

    def click(self, *locator):
        self.find_elements(*self.LOCATOR)
        self.click(*self.LOCATOR)

