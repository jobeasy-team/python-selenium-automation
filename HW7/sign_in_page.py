from selenium.webdriver.common.by import By

from pages.base_page import Page


class SignInPage(Page):
    TEXT = (By.CSS_SELECTOR, 'h1.a-spacing-small')

    def verify_signin_text(self, expected_text):
        self.verify_text(expected_text, *self.TEXT)
