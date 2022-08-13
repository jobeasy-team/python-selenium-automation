from selenium.webdriver.common.by import By

from pages.base_page import Page


class SearchResultsPage(Page):
    RESULT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")
    NAV_SUBNAV = (By.CSS_SELECTOR, "#nav-subnav[data-category='{SUBSTR}']")

    def get_subnav_locator(self, category: str):
        # (By.CSS_SELECTOR, "#nav-subnav[data-category='books']")
        return [self.NAV_SUBNAV[0], self.NAV_SUBNAV[1].replace('{SUBSTR}', category)]

    def verify_search_results(self, expected_result):
        self.verify_element_text(expected_result, *self.RESULT)

    def verify_department_selected(self, category):
        locator = self.get_subnav_locator(category)
        self.wait_for_element_appear(*locator)