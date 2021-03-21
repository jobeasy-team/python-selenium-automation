from selenium.webdriver.common.by import By
from pages.base_page import Page


class ArticlePage(Page):
    ARTICLE_HEADER = (By.ID, 'firstHeading')
    SUB_HEADER = (By.ID, 'siteSub')

    def verify_article_header(self, expected_text: str):
        self.wait_for_element_appear(*self.SUB_HEADER)
        self.verify_text(expected_text, *self.ARTICLE_HEADER)
