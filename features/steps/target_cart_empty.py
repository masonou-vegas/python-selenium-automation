from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


# @given('Open target main page')
#def open_main(context):
    # context.driver.get('https://www.target.com/')
CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
EMPTY_MESSAGE = (By.XPATH, "//a[text()='Your cart is empty']")
EMPTY_MESSAGE_BACKUP = (By.CSS_SELECTOR, ".styles_ndsHeading__HcGpD.styles_fontSize1__i0fbt.styles_x2Margin__M5gHh")
CART_ICON_BACKUP = (By.CLASS_NAME, 'styles_ndsLink__GUaai styles_onLight__QKcK7 sc-49aad5be-1 sc-55744c41-0 fPmkKx jPsZQE')

@when('Click on cart icon')
def click_cart(context):
    context.driver.find_element(*CART_ICON).click()
    sleep(3)

@then('Verify “Your cart is empty” message is shown')
def cart_is_empty(context):
    context.driver.find_element(*EMPTY_MESSAGE_BACKUP)