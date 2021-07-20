from pages.base_page import Page
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class Header(Page):
    SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
    SEARCH_ICON = (By.ID, 'nav-search-submit-button')
    Orders_link = (By.ID, 'nav-orders')
    Click_icon = (By.ID, 'nav-cart-count-container')
    Flag = (By.CSS_SELECTOR, '.icp-nav-flag.icp-nav-flag-us')
    Spanish_lang = (By. CSS_SELECTOR, "a[href='#switch-lang=es_US']")
    Department_select = (By. ID, 'searchDropdownBox')
    Cart = (By.ID, 'nav-cart-count')
    Tab = (By.XPATH, "/html/body/div[1]/header/div/div[6]/div/a[7]")



    def input_search(self, search_word):
        self.input_text(search_word, *self.SEARCH_FIELD)

    def click_search(self):
        self.click(*self.SEARCH_ICON)

    def hoover_flag_icon(self):
        flag = self.find_element(*self.Flag)
        actions = ActionChains(self.driver)
        actions.move_to_element(flag)
        actions.perform()


    def click_orders(self):
        self.click(*self.Orders_link)


    def click_icon(self):
        self.click(*self.Click_icon)


    def select_department(self):
        select = Select(self.find_element(*self.Department_select))
        select.select_by_value('search-alias=hpc')


    def verify_cart_count(self, expected_count: str):
        self.verify_text(expected_count, *self.Cart)


    def verify_spanish_lang_present(self):
        self.wait_for_element_appear(*self.Spanish_lang)


