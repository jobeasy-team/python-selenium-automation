from selenium.webdriver.common.by import By

from pages.base_page import Page


class BestsellersPage(Page):
    TOP_LINKS = (By.CSS_SELECTOR, '#zg_header a')
    HEADER = (By.CSS_SELECTOR, '#zg_banner_text')

    def open_bestsellers(self):
        self.open_url('gp/bestsellers/')

    def click_thru_top_links(self):
        top_links = self.driver.find_elements(*self.TOP_LINKS)  # [WebEl1,WebEl2, WebEl3,... ]
        print(top_links)

        for i in range(len(top_links)):  # for x from 0 to 4
            link_to_click = self.driver.find_elements(*self.TOP_LINKS)[i]
            link_text = link_to_click.text
            link_to_click.click()
            header_text = self.driver.find_element(*self.HEADER).text
            assert link_text in header_text, f'Expected {link_text} to be in {header_text}'

