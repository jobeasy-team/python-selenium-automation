from pages.base_page import Page
from selenium.webdriver.common.by import By


class CartPage(Page):
    EMPTY_TEXT_LOCATION = (By.XPATH, "//div[@id='sc-active-cart']//h2")

    def verify_text_present(self, expect_text):
        self.verify_text(expect_text, *self.EMPTY_TEXT_LOCATION)

