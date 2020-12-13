from pages.base_page import Page
from selenium.webdriver.common.by import By


class MainPage(Page):
    SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
    SEARCH_ICON = (By.XPATH, "//input[@value='Go']")

    def open_amazon(self):
        self.open_page('https://www.amazon.com/')

    def click_search_icon(self):
        self.click(*self.SEARCH_ICON)

    def input_search_word(self, search_word):
        print("in main1" + search_word)
        # self.input_text(search_word *self.SEARCH_INPUT)
        # self.driver.input_text(*self.SEARCH_INPUT)
        self.input_text(search_word, *self.SEARCH_INPUT, )

