from pages.base_page import Page
from selenium.webdriver.common.by import By

class MainPage(Page):
    locator = (By.ID, 'nav-orders')

    def open_main_page(self):
        self.open_page()



