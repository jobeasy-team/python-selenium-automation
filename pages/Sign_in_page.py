from pages.base_page import Page
from selenium.webdriver.common.by import By


class Sign_in_link(Page):
    def verify_sign_in_opened(self):
        self.open_url(url='https://www.amazon.com/ap/signin')