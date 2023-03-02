from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC

COLOR_OPTIONS = (By.CSS_SELECTOR, '#variation_color_name li')
CURRENT_COLOR = (By.CSS_SELECTOR, '#variation_color_name .selection')


@given('Open Amazon product {product_id} page')
def open_product_page(context, product_id):
    context.driver.get(f'https://www.amazon.com/gp/product/{product_id}/')


@then('Verify user can click through colors')
def verify_user_can_select_colors(context):
    all_color_options = context.driver.find_elements(*COLOR_OPTIONS)
    print(all_color_options)
    expected_colors = ['Black', 'Blue, Over Dye', 'Bright White', 'Dark Blue Vintage', 'Dark Indigo/Rinsed']

    actual_colors = []
    for color in all_color_options[:5]:
        color.click()
        current_color = context.driver.find_element(*CURRENT_COLOR).text
        # print('Current color: ', current_color)
        actual_colors.append(current_color)
        print(actual_colors)

    assert expected_colors == actual_colors, f'Expected colors are {expected_colors} and actual are {actual_colors}'
