from pages.main_page import MainPage
from pages.header import Header
from pages.search_results_page import SearchResultsPage
from pages.sign_in_page import SigninPage
from pages.cart_page import CartPage
from pages.product_search_page import ProductSearchPage
from pages.selected_product_page import SelectedProductPage

class Application:

    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.header = Header(self.driver)
        self.search_results_page = SearchResultsPage(self.driver)
        self.sign_in_page = SigninPage(self.driver)
        self.cart_page = CartPage(self.driver)
        self.product_search_page = ProductSearchPage(self.driver)
        self.selected_product_page = SelectedProductPage(self.driver)