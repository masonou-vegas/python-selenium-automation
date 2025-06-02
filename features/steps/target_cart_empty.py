from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target main page')
def open_main(context):
    context.driver.get('https://www.target.com/')


@when('Click cart icon')
def click_cart(context):
    context.driver.find_element(By.CLASS_NAME, 'styles_ndsLink__GUaai styles_onLight__QKcK7 sc-49aad5be-1 sc-55744c41-0 fPmkKx jPsZQE').click()
    sleep(1)

@then('Cart is empty')
def cart_is_empty(context):
    context.driver.find_element(By.XPATH, "//a[text()='Your cart is empty']")