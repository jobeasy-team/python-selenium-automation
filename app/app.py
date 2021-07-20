from pages.header import Header
from pages.main_page import Main
from pages.search_result import SearchResults
from pages.Sign_in_page import Sign_in_link
from pages.Shopping_cart import Shopping_Cart
from pages.product_item import SanitizerItem
from pages.clothing_page import Clothing_prod
from pages.clothing_header import Cloth_header

class App():

    def __init__(self, driver):
        self.driver = driver

        self.main_page = Main(self.driver)
        self.header = Header(self.driver)
        self.search_results_page = SearchResults(self.driver)
        self.sign_in_page = Sign_in_link(self.driver)
        self.shopping_cart = Shopping_Cart(self.driver)
        self.product_item = SanitizerItem(self.driver)
        self.clothing_page = Clothing_prod(self.driver)
        self.clothing_header = Cloth_header(self.driver)
