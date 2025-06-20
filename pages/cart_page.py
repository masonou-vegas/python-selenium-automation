from selenium.webdriver.common.by import By

from pages.base_page import Page


class CartPage(Page):
    # Copy
    cart_empty_txt = 'Your cart is empty'
    # Locators
    CART_EMPTY_MSG = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg']")
    VERIFY_PRODUCT = (By.CSS_SELECTOR, '.h-margin-b-tight h-text-grayDark ')

    def verify_cart_empty(self):
        self.verify_text(self.cart_empty_txt, *self.CART_EMPTY_MSG)

    def verify_cart_opened(self):
        # self.verify_url('https://www.target.com/cart')
        # self.verify_partial_url('/cart')
        self.wait_for_url_contains('/cart')

    def verify_product(self):
        self.find_element(*self.VERIFY_PRODUCT)