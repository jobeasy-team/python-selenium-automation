from pages.base_page import Page
from selenium.webdriver.common.by import By


class SignInPage(Page):
    EMAIL_FIELD = (By.CSS_SELECTOR, "input[type='email']")

    def verify_url(self, url=''):
        self.url = self.driver.current_url
        assert url in self.url
        # print(self.url)
        # print(url)
