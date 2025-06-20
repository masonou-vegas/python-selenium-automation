from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep

class MainPage(Page):
    CLICK_SIGN_IN_POPUP = (By.CSS_SELECTOR, "[data-test='accountNav-signIn']")
    ADD_TO_CART = (By.ID, 'addToCartButtonOrTextIdFor12959821')
    VIEW_CART = (By.CSS_SELECTOR, '.styles_ndsBaseButton__W8Gl7 styles_md__X_r95 styles_mdGap__9J0yq styles_fullWidth__3XX6f styles_ndsButtonSecondary__iSf2I')

    def open_main_page(self):
        self.driver.get('https://www.target.com/')

    def click_sign_in_popup(self):
        self.driver.find_element(*self.CLICK_SIGN_IN_POPUP).click()

    def click_add_to_cart(self):
        self.click(*self.ADD_TO_CART)

    def click_view_cart(self):
        self.click(*self.VIEW_CART)



