from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import Page
from selenium.webdriver.support.ui import Select

class Header(Page):
    SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
    SEARCH_BTN = (By.ID, 'nav-orders')
    LOCATOR   = (By.LINK_TEXT, 'Returns & Orders')
    FLAG =   (By.CSS_SELECTOR, '.icp-nav-flag-us')
    SPANISH_LANG = (By.CSS_SELECTOR, "[href='#switch-lang=es_US']")
    NEW_ARRIVALS = (By.LINK_TEXT, 'New Arrivals')
    PRODUCT  = (By.CSS_SELECTOR, '.mega-menu')
    DEPARTMENT_SELECT = (By.ID, 'searchDropdownBox')
    SELECTED_DEPARTMENT = (By.CSS_SELECTOR, '#nav-subnav')
    search_word = 'baby wipes'
    AMAZON_LINK = (By.ID, 'nav-orders')
    SIGNIN_PAGE = (By.XPATH, "//h1[@class='a-spacing-small']")
    CART_ICON  = (By.ID, 'nav-cart-count')
    EMPTY_CART_TEXT = (By.XPATH, "//div[@class='a-row sc-your-amazon-cart-is-empty']")

    def search_amazon(self, search_word):
        self.input_text(search_word, *self.SEARCH_INPUT)
        self.click(*self.SEARCH_BTN)

    #def click(self, *locator):
       #self.find_elements(*self.LOCATOR)
       #self.click(*self.LOCATOR)

    def click_amazon_orders(self):
       self.click(*self.AMAZON_LINK,)


    def click_on_cart_icon(self):
        self.click(*self.CART_ICON)


    def hover_lang(self):
        actions = ActionChains(self.driver)
        flag = self.find_element(*self.FLAG)
        actions.move_to_element(flag)
        actions.perform()


    def verify_spanish_lang(self):
        self.wait_for_element_appear(*self.SPANISH_LANG)


    def verify_signin_page(self):
        self.wait_for_element_appear(*self.SIGNIN_PAGE)


    def verify_new_arrivals(self):
        self.wait_for_element_appear(*self.PRODUCT)



    def hover_new_arrivals(self):
        actions = ActionChains(self.driver)
        new_arrivals = self.find_element(*self.NEW_ARRIVALS)
        actions.move_to_element(new_arrivals)
        actions.perform()

    def select_dept(self):
        department_select = self.find_element(*self.DEPARTMENT_SELECT)
        select = Select(department_select)
        select.select_by_value('search-alias=fashion-baby')


    def verify_department(self):
        self.wait_for_element_appear(*self.SELECTED_DEPARTMENT)

    def verify_cart_empty(self):
        self.wait_for_element_appear(*self.EMPTY_CART_TEXT)

