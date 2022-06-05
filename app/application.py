
from pages.header import Header
from pages.main_page import MainPage

from pages.amazon_order_page import Orderpage

class Application:

    def __init__(self, driver):
        self.driver = driver

        self.amazon_order_page = Orderpage(self.driver)
        self.header = Header(self.driver)
        self.main_page = MainPage(self.driver)


