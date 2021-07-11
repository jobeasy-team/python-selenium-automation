from selenium.webdriver.common.by import By
from behave import given, when, then

@given('Open Amazon product page')
def open_product_page(context):
    context.driver.get('https://www.amazon.com/dp/B081YS2F7N')

@then('Verify if user can see colors on product')
def verify_color_count(context):
    expected_colors = ['Black', 'Blue', 'Burgundy', 'Caramel', 'Gray', 'Green', 'Khaki', 'Pink', 'White', 'Yellow']
    color_web_elements = context.driver.find_elements(By. CSS_SELECTOR, "#variation_color_name li")

    for i in range(len(color_web_elements)):
        color_web_elements[i].click()
        actual_text = context.driver.find_element(By. CSS_SELECTOR, "#variation_color_name span.selection").text
        assert actual_text == expected_colors[i], f'Error, color is {actual_text}, but expected {expected_colors[i]}'

