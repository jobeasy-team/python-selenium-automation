from selenium.webdriver.common.by import By

from pages.base_page import Page


class SearchResultsPage(Page):
    SEARCH_RESULT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")

    def verify_search_result(self, verify_text):
        result = self.driver.find_element(*self.SEARCH_RESULT)
        assert result.text == verify_text, f'Error.Expected Dress, but got {result.text}'

