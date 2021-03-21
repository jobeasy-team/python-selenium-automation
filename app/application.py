from pages.article_page import ArticlePage
from pages.base_page import Page
from pages.main_page import MainPage
from pages.no_search_results_page import NoSearchResults
from pages.right_navigation import RightNavigation


class Application:

    def __init__(self, driver):
        self.driver = driver
        self.page = Page(self.driver)
        self.article_page = ArticlePage(self.driver)
        self.main_page = MainPage(self.driver)
        self.no_search_results_page = NoSearchResults(self.driver)
        self.right_navigation = RightNavigation(self.driver)

