from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep

class SignIn(Page):
    SIGN_IN_TEXT = (By.CSS_SELECTOR, ".styles_ndsHeading__HcGpD.styles_fontSize1__i0fbt.styles_x2Margin__M5gHh.h-text-lg.h-text-center.h-margin-b-tiny")
    EMAIL = (By.ID, "username")
    TERMS_LINK = (By.CSS_SELECTOR, '[aria-label="terms & conditions - opens in a new window"]')
    def verify_sign_in(self):
        self.find_element(*self.SIGN_IN_TEXT)

    def input_email(self, email):
        self.input_text(email, *self.EMAIL)

    def open_sign_in_page(self):
        self.driver.get('https://www.target.com/orders?lnk=acct_nav_my_account')

    def store_original_window(self):
        self.get_current_window_id()

    def click_on_target_terms_and_conditions_link(self):
        self.click(*self.TERMS_LINK)

