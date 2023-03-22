from selenium.webdriver.common.by import By
from pages.base_page import Page


class SigninPage(Page):

    def verify_signin_opened(self):
        self.verify_url_contains_query('https://www.amazon.com/ap/signin')