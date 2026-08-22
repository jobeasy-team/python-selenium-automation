from pages.base_page import Page

class PrivacyPage(Page):

    def verify_pp_page_opened(self):
        self.verify_partial_url('target-privacy-policy')