from selenium.webdriver.common.by import By
from pages.base_page import Page


class SignInPage(Page):
    RETURNS_ORDERS = (By.CSS_SELECTOR, "h1[class='a-spacing-small']")

    def verify_sign_in_page(self, find_text):
        self.verify_result_text(find_text, *self.RETURNS_ORDERS)