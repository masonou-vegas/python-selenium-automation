from pages.base_page import Page

class TermsPage(Page):
    def verify_terms_and_conditions_page_is_opened(self):
        self.wait_for_url_contains('terms-conditions')
