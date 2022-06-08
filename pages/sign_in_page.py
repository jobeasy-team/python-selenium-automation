from selenium.webdriver.common.by import By

from pages.base_page import Page


class SignInPage(Page):
    Sign_in_text = (By.CSS_SELECTOR, 'h1')

    def ver_sign_in_page(self, exp_res):
        self.verify_text(exp_res, *self.Sign_in_text)
