from pages.base_page import Page
from selenium.webdriver.common.by import By


class SearchResults(Page):
    SEARCH_RESULT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")
    Product_result = (By.XPATH, "//h2[contains(@class, 'a-size-mini a-spacing-none a-color-base s-line-clamp-4')]")
    HPC = (By.CSS_SELECTOR, "#nav-subnav[data-category='hpc']")

    def verify_search_worked(self):
        self.verify_text('"Table"', *self.SEARCH_RESULT)

    def click_first_product(self):
        self.click(*self.Product_result)

    def verify_hpc_department(self):
        self.find_element(*self.HPC)
