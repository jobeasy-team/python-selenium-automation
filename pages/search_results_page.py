from selenium.webdriver.common.by import By

from pages.base_page import Page


class SearchResultsPage(Page):
    searchResult_txt = (By.CSS_SELECTOR, 'span.a-color-state.a-text-bold')
    amzn_choice = (By.CSS_SELECTOR, 'div.a-section.a-spacing-base')

    def ver_search_results(self, exp_res):
        self.verify_text(exp_res, *self.searchResult_txt)

    def select_item(self):
        self.click(*self.amzn_choice)
