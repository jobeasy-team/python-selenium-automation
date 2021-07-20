from pages.base_page import Page
from selenium.webdriver.common.by import By

class Clothing_prod(Page):
    def open_cloth_page(self):
        self.open_url(url='https://www.amazon.com/gp/product/B074TBCSC8')