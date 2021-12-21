from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from behave import given, when, then


COLOR_OPTIONS=(By.CSS_SELECTOR, '#variation_color_name li')
SELECTED_COLOR=(By.CSS_SELECTOR,'#variation_color_name .selection')


@given('Open Amazon product {product_id} page')
def open_amazon_product_page(context, product_id):
    context.driver.get(f'https://www.amazon.com/dp/{product_id}/')


@then('Verify user can click colors')
def verify_user_can_click_colors(context):
    expected_colors = ['(PRODUCT)RED', 'Abyss Blue', 'Blue Jay', 'Chalk Pink', 'Clover','Marigold','Midnight','Pink Pomelo']

    colors = context.driver.find_elements(*COLOR_OPTIONS)
    for i in range(len(colors)):
        colors[i].click()
        actual_color= context.driver.find_element(*SELECTED_COLOR).text

        assert actual_color == expected_colors[i], f'Expected {expected_colors[i]}, but turned {actual_color}'



















