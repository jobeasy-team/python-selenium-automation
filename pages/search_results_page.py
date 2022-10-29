from selenium.webdriver.common.by import By

from pages.base_page import Page


class SearchResultsPage(Page):
    SEARCH_RESULTS = (By.CSS_SELECTOR, '.a-color-state.a-text-bold')
    SELECTED_DEPARTMENT = (By.CSS_SELECTOR, '#nav-subnav[data-category="{SUBSTR}"]')

    def get_department_locator(self, department: str):
        # department = books
        # [ By.CSS_SELECTOR , '#nav-subnav[data-category="books"]'
        return [self.SELECTED_DEPARTMENT[0], self.SELECTED_DEPARTMENT[1].replace('{SUBSTR}', department)]

    def verify_search_results(self, expected_result):
        self.verify_element_text(expected_result, *self.SEARCH_RESULTS)

    def verify_department(self, department):
        print('department => ', department)
        department_locator = self.get_department_locator(department)
        print(department_locator)
        self.wait_for_element_appear(*department_locator)

