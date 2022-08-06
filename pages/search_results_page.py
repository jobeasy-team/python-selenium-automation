from selenium.webdriver.common.by import By

from pages.base_page import Page


class SearchResultsPage(Page):
    RESULT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")

    def verify_search_results(self, expected_result):
        self.verify_element_text(expected_result, *self.RESULT)
