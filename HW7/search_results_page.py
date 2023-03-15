from pages.base_page import Page
from selenium.webdriver.common.by import By


class SearchResultsPage(Page):
    SEARCH_RESULT = (By.XPATH, '//span[@class="a-color-state a-text-bold"]')
    PRODUCT_PRICE = (By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a-price']]")

    def verify_search_result(self, expected_text):
        self.verify_text(expected_text, *self.SEARCH_RESULT)

    def click_first_product(self):
        self.wait_for_element_click(*self.PRODUCT_PRICE)
