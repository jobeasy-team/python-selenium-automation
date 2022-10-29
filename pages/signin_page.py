from selenium.webdriver.common.by import By

from pages.base_page import Page


class SignInPage(Page):
    SIGNIN_HEADER = (By.XPATH, "//h1[@class='a-spacing-small']")
    EMAIL_FIELD = (By.ID, 'ap_email')

    def verify_signin_opened(self):
        self.verify_element_text('Sign in', *self.SIGNIN_HEADER)
        # Verify email field present
        assert self.find_element(*self.EMAIL_FIELD).is_displayed()
        # self.verify_url_contains_query('https://www.amazon.com/ap/signin')
