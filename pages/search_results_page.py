from selenium.webdriver.common.by import By
from pages.base_page import Page


class SearchResultsPage(Page):
    SEARCH_RESULT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")
    SUBNAV = (By.CSS_SELECTOR, "#nav-subnav[data-category='{CATEGORY}']")

    # Dynamic locators
    def get_subnav_locator(self, category):
        # (By.CSS_SELECTOR, "#nav-subnav[data-category='{CATEGORY}']")
        # =>
        # (By.CSS_SELECTOR, "#nav-subnav[data-category=books]")
        return [self.SUBNAV[0], self.SUBNAV[1].replace('{CATEGORY}', category)]

    def verify_search_result(self, expected_text):
        self.verify_text(expected_text, *self.SEARCH_RESULT)

    def verify_selected_dept(self, category):
        locator = self.get_subnav_locator(category)
        print(locator)
        self.wait_for_element_appear(*locator)
