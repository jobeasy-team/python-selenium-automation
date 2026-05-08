from selenium.webdriver.common.by import By

from pages.base_page import Page

class SearchResultsPage(Page):
    SEARCH_RESULT_COUNT_TEXT = (By.XPATH, "//div[contains(@class, 'styles_resultCount')]")
    FAV_ICON = (By.CSS_SELECTOR, '[data-test="FavoritesButton"]')
    FAV_TT = (By.XPATH, "//*[contains(text(), 'Click to sign in and save')]")

    def hover_fav_icon(self):
        self.hover_element(*self.FAV_ICON)

    def verify_fav_tooltip(self):
        self.wait_until_appear(*self.FAV_TT)

    def verify_search_results(self, product: str):
        self.verify_partial_text(product, *self.SEARCH_RESULT_COUNT_TEXT)

    def verify_url_product(self, product):
        self.wait_until_url_contains(product)
