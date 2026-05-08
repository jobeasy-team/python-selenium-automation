from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from pages.base_page import Page


class HelpPage(Page):
    SELECT_TOPIC_DD = (By.CSS_SELECTOR, "select[id*='ViewHelpTopics']")

    RETURNS_HEADER = (By.XPATH, "//h1[text()=' Returns']")
    PROMOTIONS_HEADER = (By.XPATH, "//h1[text()=' Current promotions']")
    ABOUT_TARGET_CIRCLE_HEADER = (By.XPATH, "//h1[text()=' About Target Circle']")
    # Dynamic locator => modify locator od the el during the test execution
    HEADER = (By.XPATH, "//h1[text()=' {SUBSTR}']")

    def get_header_locator(self, expected_text):
        # return [By.XPATH ,    "//h1[text()=' expected_text']
        return [self.HEADER[0], self.HEADER[1].replace('{SUBSTR}', expected_text)]

    def open_help_returns(self):
        self.driver.get('https://help.target.com/help/SubCategoryArticle?childcat=Returns&parentcat=Returns+%26+Exchanges')

    def select_topic(self, topic):
        dropdown = self.find_element(*self.SELECT_TOPIC_DD)
        select = Select(dropdown)
        select.select_by_value(topic)

    def verify_header_present(self, expected_text):
        locator = self.get_header_locator(expected_text)
        self.wait_until_appear(*locator)

    # def verify_promotions_opened(self):
    #     self.wait_until_appear(*self.PROMOTIONS_HEADER)
    #
    # def verify_returns_opened(self):
    #     self.wait_until_appear(*self.RETURNS_HEADER)
    #
    # def verify_about_target_circle_opened(self):
    #     self.wait_until_appear(*self.ABOUT_TARGET_CIRCLE_HEADER)
