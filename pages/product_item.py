from pages.base_page import Page
from selenium.webdriver.common.by import By


class SanitizerItem(Page):
    First_product = (By.XPATH, "//div[@data-asin='B076BTZT9R']")

    def click_on_item(self):
        self.click(*self.First_product)