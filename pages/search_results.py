from pages.base_page import Page
from selenium.webdriver.common.by import By


class SearchResultsPage(Page):
    TOOLBAR_TEXT_BOLD = (By.CSS_SELECTOR, "h1 span.a-text-bold")

    def verify_result_shown(self, expected_text):
        self.verify_text(expected_text, *self.TOOLBAR_TEXT_BOLD)
