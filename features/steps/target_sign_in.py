from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep




@given('Open target main home page')
def open_main(context):
    context.driver.get('https://www.target.com/')


@then('Click sign in on homepage')
def click_sign_in_homepage(context):
    context.driver.find_element(By.ID, 'account-sign-in').click()
    sleep(1)
@then('Click sign in on pop up')
def click_sign_in_pop(context):
    context.driver.find_element(By.XPATH, "//a[text()='Sign in or create account']").click()
    sleep(5)

@then('Sign in form displays')
def sign_in_form(context):
    context.driver.find_element(By.XPATH, "//a[text()='Sign in or create account']")
    context.driver.find_element(By.XPATH, "//a[text()='Enter your email or mobile number to continue']")