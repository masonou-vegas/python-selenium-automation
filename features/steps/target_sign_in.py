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

@given('Open sign in page')
def open_sign_in_page(context):
    context.app.sign_in_page.open_sign_in_page()

@when('Store original window')
def store_original_window(context):
    context.original_window = context.app.sign_in_page.store_original_window()

@then('Click on Target terms and conditions link')
def click_on_target_terms_and_conditions_link(context):
    context.app.sign_in_page.click_on_target_terms_and_conditions_link()

@then('Switch to the newly opened window')
def switch_to_newly_opened_window(context):
    context.app.base_page.switch_to_new_window()

@then('Verify Terms and Conditions page is opened')
def verify_terms_and_conditions_page_is_opened(context):
    context.app.terms_and_conditions_page.verify_terms_and_conditions_page_is_opened()

@then('User can close new window and switch back to original')
def user_close_new_window(context):
    context.app.base_page.close_window()
    sleep(1)
    context.app.base_page.switch_to_window_by_id(context.original_window)




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
