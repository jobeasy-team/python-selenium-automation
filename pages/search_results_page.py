from selenium.webdriver.common.by import By

from pages.base_page import Page

class SearchResultsPage(Page):
    RESULTS_COUNT_TXT = (By.CSS_SELECTOR, "[data-test='lp-resultsCount']")

    def verify_search_result_shown(self, expected_product):
        self.verify_partial_element_text(expected_product, *self.RESULTS_COUNT_TXT)

    def verify_search_results_url(self, expected_partial_url):
        self.verify_partial_url(expected_partial_url)