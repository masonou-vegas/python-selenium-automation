from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep

class SignIn(Page):
    SIGN_IN_TEXT = (By.CSS_SELECTOR, ".styles_ndsHeading__HcGpD.styles_fontSize1__i0fbt.styles_x2Margin__M5gHh.h-text-lg.h-text-center.h-margin-b-tiny")
    EMAIL = (By.ID, "username")
    def verify_sign_in(self):
        self.find_element(*self.SIGN_IN_TEXT)

    def input_email(self, email):
        self.input_text(email, *self.EMAIL)
