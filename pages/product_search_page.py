from selenium.webdriver.common.by import By
from pages.base_page import Page


class ProductSearchPage(Page):
    FIRST_PRODUCT = (By.CSS_SELECTOR, "span.a-size-base-plus.a-color-base.a-text-normal")

    def click_first_product(self):
        self.click(*self.FIRST_PRODUCT)
