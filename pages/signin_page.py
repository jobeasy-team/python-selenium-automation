from selenium.webdriver.common.by import By

from pages.base_page import Page


class SignInPage(Page):
    SIGNIN_HEADER = (By.XPATH, "//h1[@class='a-spacing-small']")
    EMAIL_FIELD = (By.ID, 'ap_email')

    def verify_signin_opened(self):
        # expected_text = 'Sign-In'
        # actual_text = self.find_element(*self.SIGNIN_HEADER).text
        # assert actual_text == expected_text, f'Expected {expected_text} but got {actual_text}'
        # # Verify email field present
        # assert self.find_element(*self.EMAIL_FIELD).is_displayed()
        #
        self.verify_url_contains_query('https://www.amazon.com/ap/signin')
