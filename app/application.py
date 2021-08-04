from pages.header import Header
from pages.main_page import Main
from pages.search_results import SearchResults


class Application:

    def __init__(self, driver):
        self.driver = driver

        self.main_page = Main(self.driver)
        self.header = Header(self.driver)
        self.search_results = SearchResults(self.driver)
