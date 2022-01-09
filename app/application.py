from pages.main_page import MainPage
from pages.signin_page import Signin
from pages.cart_page import CartPage
from pages.header import Header
from pages.search_result_page import SearchResult


class Application:

    def __init__(self, driver):
        self.main_page = MainPage(driver)
        self.signin_page = Signin(driver)
        self.cart_page = CartPage(driver)
        self.header = Header(driver)
        self.search_result = SearchResult(driver)