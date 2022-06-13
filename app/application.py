# Create a class that links pageObjects with behave contexts
from pages.header import Header
from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage
from pages.sign_in_page import SignInPage
from pages.cart_page import Cart


class Application:

    def __init__(self, driver):
        self.driver = driver

        self.header = Header(self.driver)
        self.main_page = MainPage(self.driver)
        self.search_results_page = SearchResultsPage(self.driver)
        self.sign_in_page = SignInPage(self.driver)
        self.cart_page = Cart(self.driver)


# a variable can be created iot access all methods within the classes
# open enviornment.py and create a context variable for Application class
# a = Application()
