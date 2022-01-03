from pages.base_page import Page


class Signin(Page):
    query = 'signin'

    def verify_url_contains_signin(self):
        self.verify_url_contains_query(self.query)
