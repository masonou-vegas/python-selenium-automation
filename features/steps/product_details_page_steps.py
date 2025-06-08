from selenium.webdriver.common.by import By
from behave import given, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


COLOR_OPTIONS = (By.CSS_SELECTOR, "li[class*='CarouselItem'] img")
SELECTED_COLOR = (By.CSS_SELECTOR, "[data-test='@web/VariationComponent'] div")
WRANGLER_COLOR = (By.CSS_SELECTOR, "[class*='styles_headerWrapper__Xzdtg']")


@given('Open target product A-91269718 page')
def open_target(context):
    context.driver.get(f'https://www.target.com/p/wranglers-men-39-s-relaxed-fit-straight-jeans/-/A-91269718?preselect=90919011#lnk=sametab')
    sleep(8)


@then('Verify user can click through colors')
def click_and_verify_colors(context):
    expected_colors = ['Navy Denim', 'Dark Wash', 'Light Wash']
    actual_colors = []

    colors = context.driver.find_elements(*COLOR_OPTIONS)  # [webelement1, webelement2, webelement3]
    print(colors)

    for c in colors:
        c.click()

        selected_color = context.driver.find_element(*SELECTED_COLOR).text  # 'Color\nBlack'
        print('Current color', selected_color)

        selected_color = selected_color.split('\n')[1]  # remove 'Color\n' part, keep Black'
        actual_colors.append(selected_color)
        print(actual_colors)

    assert expected_colors == actual_colors, f'Expected {expected_colors} did not match actual {actual_colors}'

@given('Open target product A-54551690 page')
def open_target_wranglers(context):
        context.driver.get(
            f'https://www.target.com/p/denizen-from-levi-s-men-s-232-slim-straight-fit-jeans/-/A-54551728?preselect=53715600#lnk=sametab')
        context.driver.wait.until(
        EC.visibility_of_element_located(WRANGLER_COLOR),
        message='Product name was not visible'
    )
        #Need a sleep because of random popup
        sleep(8)
@then('Verify user can click through A-54551690 colors')
def click_and_verify_wrangler_colors(context):

    expected_colors = ['30x30', '30x30', '30x30', '30x30']
    actual_wrangler_colors = []

    colors = context.driver.find_elements(*COLOR_OPTIONS)  # [webelement1, webelement2, webelement3, webelement4]
    print(colors)

    for c in colors:
        c.click()

        selected_color = context.driver.find_element(*SELECTED_COLOR).text  # 'Color\nBlack'
        print('Current color', selected_color)

        selected_color = selected_color.split('\n')[1]  # remove 'Color\n' part, keep Black'
        actual_wrangler_colors.append(selected_color)
        print(actual_wrangler_colors)

    assert expected_colors == actual_wrangler_colors, f'Expected {expected_colors} did not match actual {actual_wrangler_colors}'