from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import Page
from selenium.webdriver.support.ui import Select

class Header(Page):
    SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
    SEARCH_BTN = (By.ID, 'nav-orders')
    LOCATOR   = (By.ID, 'nav-orders')
    FLAG =   (By.CSS_SELECTOR, '.icp-nav-flag-us')
    SPANISH_LANG = (By.CSS_SELECTOR, "[href='#switch-lang=es_US']")
    NEW_ARRIVALS = (By.LINK_TEXT, 'New Arrivals')
    PRODUCT  = (By.CSS_SELECTOR, '.mega-menu')
    DEPARTMENT_SELECT = (By.ID, 'searchDropdownBox')
    SELECTED_DEPARTMENT = (By.CSS_SELECTOR, '#nav-subnav')
    search_word = 'baby wipes'

    def search_amazon(self, search_word):
        self.input_text(search_word, *self.SEARCH_INPUT)
        self.click(*self.SEARCH_BTN)

    def click(self, *locator):
        self.find_elements(*self.LOCATOR)
        self.click(*self.LOCATOR)


    def hover_lang(self):
        actions = ActionChains(self.driver)
        flag = self.find_element(*self.FLAG)
        actions.move_to_element(flag)
        actions.perform()


    def verify_spanish_lang(self):
        self.wait_for_element_appear(*self.SPANISH_LANG)


    def verify_new_arrivals(self):
        self.wait_for_element_appear(*self.PRODUCT)



    def hover_new_arrivals(self):
        actions = ActionChains(self.driver)
        new_arrivals = self.find_element(*self.NEW_ARRIVALS)
        actions.move_to_element(new_arrivals)
        actions.perform()

    def select_dept(self):
        department_select = self.find_elements(*self.DEPARTMENT_SELECT)
        select = Select(department_select)
        select.select_by_value('search-alias=fashion-baby')


    def verify_department(self):
        self.wait_for_element_appear(*self.SELECTED_DEPARTMENT)
