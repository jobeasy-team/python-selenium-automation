from selenium.webdriver.common.by import By
from behave import given, then

colors_array = (By.CSS_SELECTOR, '#variation_color_name li')
selected_color = (By.CSS_SELECTOR, '#variation_color_name .selection')


@given('Open Amazon product {item} page')
def open_amazon(context, item):
    context.driver.get(f'https://www.amazon.com/gp/product/{item}/')


@then('Verify user can click through colors')
def verify_can_click_through_colors(context):
    expected_colors = ['Black', 'Dark Blue Vintage', 'Dark Indigo/Rinsed']
    for i in range(len(expected_colors)):
        context.driver.find_elements(*colors_array)[i].click()
        actual_color = context.driver.find_element(*selected_color).text
        assert actual_color == expected_colors[i], f'Expected {expected_colors}, but it shows {actual_color}'
