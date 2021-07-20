from pages.base_page import Page
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

class Cloth_header(Page):
    Tab = (By.CSS_SELECTOR, "#nav-subnav a.nav-hasArrow[href*='/s/ref']")
    Women_section = (By.CSS_SELECTOR, "a.mm-merch-panel[href*='/s?i=fashion-womens']")


    def hoover_tab(self):
        tab = self.find_element(*self.Tab)
        actions = ActionChains(self.driver)
        actions.move_to_element(tab)
        actions.perform()


    def verify_women_section(self):
        self.wait_for_element_appear(*self.Women_section)