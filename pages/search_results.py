from pages.base_page import Page
from selenium.webdriver.common.by import By

class SearchResults(Page):
    SEARCH_RESULT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")

    def verify_search_worked(self):
        self.verify_text("Table", *self.SEARCH_RESULT)