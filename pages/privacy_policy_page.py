from pages.base_page import Page


class PrivacyPolicyPage(Page):

    def verify_pp_opened(self):
        self.wait_for_url_contains('target-privacy-policy')
