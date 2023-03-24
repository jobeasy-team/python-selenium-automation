from support.logger import logger
from pages.base_page import Page


class MainPage(Page):

    def open_main_url(self):
        logger.info('Opening url https://www.amazon.com/...')
        self.open_url('https://www.amazon.com/')