from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open target main page')
def open_main_page(context):
    context.driver.get('https://www.target.com/')

@when('Click add to cart')
def click_add_to_cart(context):
    context.driver.find_element(By.ID, 'addToCartButtonOrTextIdFor94445278').click()

sleep(2)

@then('Click add to cart from popup')
def click_add_to_cart_popup(context):
    context.driver.find_element(By.ID, 'addToCartButtonOrTextIdFor94189803').click()

sleep(2)

@then('Click view cart')
def click_view_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, '.styles_ndsBaseButton__W8Gl7 styles_md__X_r95 styles_mdGap__9J0yq styles_fullWidth__3XX6f styles_ndsButtonSecondary__iSf2I').click()
sleep(2)
@then('Verify product is in cart')
def verify_product(context):
    context.driver.find_element(By.CSS_SELECTOR, '.h-margin-b-tight h-text-grayDark ')