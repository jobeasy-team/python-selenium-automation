from pages.main_page import MainPage
from pages.search_results import SearchResultsPage
from pages.shopping_cart_page import ShoppingCart
from pages.sign_in_page import SignInPage
from pages.side_menu import SideMenu


class Application:
    def __init__(self, driver):
        self.driver = driver

        self.main_page = MainPage(self.driver)
        self.search_results = SearchResultsPage(self.driver)
        self.shopping_cart_page = ShoppingCart(self.driver)
        self.sign_in_page = SignInPage(self.driver)
        self.side_menu = SideMenu(self.driver)

