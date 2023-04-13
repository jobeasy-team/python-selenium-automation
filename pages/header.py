from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


class Header(Page):
    AMAZON_SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
    SEARCH_ICON = (By.ID, 'nav-search-submit-button')
    ORDERS = (By.ID, 'nav-orders')
    CART = (By.CSS_SELECTOR, "#nav-cart-count")
    DEPARTMENT_SELECTION = (By.ID, 'searchDropdownBox')
    # OPTIONS = (By.)
    # X = (By.)

    def input_search_text(self, text):
        self.input_text(text, *self.AMAZON_SEARCH_FIELD)

    def click_search(self):
        self.click(*self.SEARCH_ICON)

    def click_orders(self):
        self.click(*self.ORDERS)

    def click_cart(self):
        self.click(*self.CART)

    def hover_options(self):
        options = self.find_element(*self.OPTIONS)
        actions = ActionChains(self.driver)
        actions.move_to_element(options)
        actions.perform()

    def select_department(self, alias):
        department_drop_down = self.find_element(*self.DEPARTMENT_SELECTION)
        select = Select(department_drop_down)
        select.select_by_value(f'search-alias={alias}')

    def verify_x_shows(self):
        self.wait_for_element_appear(*self.X)