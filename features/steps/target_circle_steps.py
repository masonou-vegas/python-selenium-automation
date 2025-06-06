from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open target circle homepage')
def open_main_circle(context):
    context.driver.get('https://www.target.com/circle/')

@then('Verify at least {number} benefit cells')
def verify_at_least_benefit_cells(context, number):
    cells = context.driver.find_elements(By.CSS_SELECTOR, '[class*="cell-item-content"')
    print(cells)
    assert len(cells) >= int(number)