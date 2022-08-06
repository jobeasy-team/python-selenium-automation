from pages.base_page import Page


class BestsellersPage(Page):

    def open_bestsellers(self):
        self.open_url(end_url='gp/bestsellers')
