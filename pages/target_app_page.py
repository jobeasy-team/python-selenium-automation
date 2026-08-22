from selenium.webdriver.common.by import By

from pages.base_page import Page

class TargetAppPage(Page):
    PRIVACY_LINK = (By.CSS_SELECTOR, "a[class*='privacyPolicyLink']")

    def open_target_app_page(self):
        self.open_url('c/target-app/-/N-4th2r')

    def click_pp_link(self):
        self.click(*self.PRIVACY_LINK)