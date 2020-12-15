from pages.base_page import Page


class HamburgerMenu(Page):
    def click_menu_item(self, *locator):
        self.click(*locator)

    def verify_links(self, link_count, *locator):
        self.verify_link_count(link_count, *locator)
