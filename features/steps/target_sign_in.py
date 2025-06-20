from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep




# @given('Open target main home page')
# def open_main(context):
#     context.driver.get('https://www.target.com/')


#@then('Click sign in on homepage')
# def click_sign_in_homepage(context):
#     context.driver.find_element(By.ID, 'account-sign-in').click()
#     sleep(1)
# @then('Click sign in on pop up')
# def click_sign_in_pop(context):
#     context.driver.find_element(By.XPATH, "//a[text()='Sign in or create account']").click()
#     sleep(5)

@then('Sign in form displays')
def sign_in_form(context):
    context.app.sign_in_page.verify_sign_in()
    # context.driver.find_element(By.XPATH, "//a[text()='Sign in or create account']")
    # context.driver.find_element(By.XPATH, "//a[text()='Enter your email or mobile number to continue']")

@when('Input {email}')
def input_email(context, email):
    context.app.sign_in_page.input_email(email)

# @when('Click continue button')
# def click_sign_in_button(context):
#     context.app.sign_in_page.
#
# @when('Input password')
# def input_password(context):
#     context.app.sign_in_page
#
# @when('Click sign in with password button')
# def click_sign_in_button(context):
#     context.app.sign_in_page
#
# @then('User is logged in')
# def user_is_logged_in(context):
#     context.app.sign_in_page
