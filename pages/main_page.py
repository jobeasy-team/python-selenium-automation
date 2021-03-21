from selenium.webdriver.common.by import By
from pages.base_page import Page


class MainPage(Page):
    LOGO = (By.ID, 'p-logo')
    HEADER = (By.ID, 'mw-head')
    NAVIGATION = (By.ID, 'p-navigation')
    WELCOME_HEADER = (By.ID, 'mp-welcome')
    FREE_CONTENT = (By.ID, 'mp-free')
    ARTICLE_COUNT = (By.ID, 'articlecount')

    def open_page(self):
        self.open_url('wiki/Main_Page')

    def verify_ui_elements(self):
        self.wait_for_element_appear(*self.LOGO)
        self.wait_for_element_appear(*self.HEADER)
        self.wait_for_element_appear(*self.NAVIGATION)
        self.wait_for_element_appear(*self.WELCOME_HEADER)
        self.wait_for_element_appear(*self.FREE_CONTENT)
        self.wait_for_element_appear(*self.ARTICLE_COUNT)