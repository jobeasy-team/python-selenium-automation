from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class Header(Page):
    CATEGORY = (By.ID, "searchDropdownBox")


def select_department(self):
    dropdown = self.find_element(*self.CATEGORY)
    select = Select(dropdown)
    select.select_by_value('search-alias=baby-products')