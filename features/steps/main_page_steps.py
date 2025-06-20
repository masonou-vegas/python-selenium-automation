from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open target main page')
def open_main(context):
    #context.driver.get('https://www.target.com/')
    #context.driver.get('https://www.target.com/')
    context.app.main_page.open_main_page()

@then('Click sign in on pop up')
def click_sign_in_pop(context):
    context.app.main_page.click_sign_in_popup()
    # context.driver.find_element(By.CSS_SELECTOR, "[data-test='accountNav-signIn']").click()
    # sleep(5)