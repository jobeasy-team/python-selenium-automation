from selenium.webdriver.common.by import By

from pages.base_page import Page

class OrderPage(Page):
    LOCATOR = (By.ID, 'nav-orders')

    def click_amazonorders(self):

            self.find_elements(*self.LOCATOR)
            self.click(*self.LOCATOR)


    def verify_orders(self):
        pass