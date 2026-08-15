from selenium.webdriver.common.by import By

from pages.base_page import Page

class SearchResultsPage(Page):
    RESULTS_COUNT_TXT = (By.CSS_SELECTOR, "[data-test='lp-resultsCount']")

    def verify_search_result_shown(self, expected_product):
        actual_text = self.get_element_text(*self.RESULTS_COUNT_TXT)
        assert expected_product in actual_text, f'Expected text {expected_product} not in actual {actual_text}'
