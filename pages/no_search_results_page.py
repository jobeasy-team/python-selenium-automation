from time import sleep
from selenium.webdriver.common.by import By
from pages.base_page import Page


class NoSearchResults(Page):
    SEARCH_FORM = (By.ID, 'search')
    CREATE_PAGE_MSG = (By.CSS_SELECTOR, 'p.mw-search-createlink')
    CREATE_PAGE_LINK = (By.CSS_SELECTOR, "a[href*='Articles_for_creation']")

    def click_create_page(self):
        sleep(1)
        self.wait_for_element_appear(*self.SEARCH_FORM)
        self.wait_for_element_click(*self.CREATE_PAGE_LINK)
        self.wait_for_url_change()

    def verify_page_opened(self):
        self.verify_url_contains_query(f'{self.base_url}w/index.php?search=')
        self.wait_for_element_appear(*self.SEARCH_FORM)
