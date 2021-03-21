from selenium.webdriver.common.by import By
from pages.base_page import Page


class RightNavigation(Page):
    SEARCH_FIELD = (By.ID, 'searchInput')
    SEARCH_ICON = (By.ID, 'searchButton')

    def search(self, query: str):
        self.input_text(query, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_ICON)
        self.wait_for_url_change()
