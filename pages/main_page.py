from pages.base_page import Page
from selenium.webdriver.common.by import By

class Main(Page):
    def open_main(self):
        self.open_url(url='https://www.amazon.com/')

#class Clothing_prod(Page):
##        self.open_url(url='https://www.amazon.com/gp/product/B074TBCSC8')