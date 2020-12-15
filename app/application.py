from pages.hamburger_menu_page import HamburgerMenu
from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage
from pages.shopping_empty_page import ShoppingEmpty
from pages.sign_in_page import SignInPage


class Application:

    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.search_results_page = SearchResultsPage(self.driver)
        self.sign_in_page = SignInPage(self.driver)
        self.shopping_empty_page = ShoppingEmpty(self.driver)
        self.hamburger_menu_page = HamburgerMenu(self.driver)

