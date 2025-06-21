from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep
from pages.base_page import Page


class HelpPage(Page):
    # RETURNS_HEADER = (By.XPATH, "//h1[text()=' Returns']")
    # PROMOTIONS_HEADER = (By.XPATH, "//h1[text()=' Current promotions']")
    HEADER = (By.XPATH, "//h1[text()=' {SUBSTR}']")
    SELECT_DD = (By.CSS_SELECTOR, "select[id*='viewHelpTopics']")

    # Dynamic locator => generating locator during TC execution
    # if expected_text = Returns:
    # (By.XPATH, "//h1[text()=' {SUBSTR}']") => (By.XPATH, "//h1[text()=' Returns']")
    def _get_header_locator(self, expected_text):
        return [self.HEADER[0], self.HEADER[1].replace('{SUBSTR}', expected_text)]

    def open_help_returns(self):
        self.driver.get('https://help.target.com/help/SubCategoryArticle?childcat=Returns&parentcat=Returns+%26+Exchanges')
        sleep(3)

    def select_promotions(self, value):
        dd = self.find_element(*self.SELECT_DD)
        select = Select(dd)
        select.select_by_value(value)

    def verify_help_page_opened(self, expected_text):
        locator = self._get_header_locator(expected_text)
        self.wait_for_element(*locator)

    # def verify_returns_opened(self):
    #     self.wait_for_element(*self.RETURNS_HEADER)
    #
    # def verify_promotions_opened(self):
    #     self.wait_for_element(*self.PROMOTIONS_HEADER)