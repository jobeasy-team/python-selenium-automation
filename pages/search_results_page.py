from selenium.webdriver.common.by import By

from pages.base_page import Page


class SearchResultsPage(Page):
    SEARCH_RESULTS_TXT = (By.XPATH, "//div[@data-test='lp-resultsCount']")

    def verify_search_results(self):
        actual_text = self.find_element(*self.SEARCH_RESULTS_TXT).text
        assert 'tea' in actual_text, f"Error, expected 'tea' not in actual {actual_text}"

