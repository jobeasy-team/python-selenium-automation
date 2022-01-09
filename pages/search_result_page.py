from pages.base_page import Page
from selenium.webdriver.common.by import By


class SearchResult(Page):
    BABY_SUB_NAV = (By.CSS_SELECTOR, "#nav-subnav[data-category='baby-products']")

    def get_category_locator(self, category):


    def verify_correct_department(self, category):
        self.wait_for_element_appear(*self.BABY_SUB_NAV)