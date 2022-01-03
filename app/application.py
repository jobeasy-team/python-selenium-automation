from pages.main_page import MainPage
from pages.signin_page import Signin
from pages.cart_page import CartPage


class Application:

    def __init__(self, driver):
        self.main_page = MainPage(driver)
        self.signin_page = Signin(driver)
        self.cart_page = CartPage(driver)