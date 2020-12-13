from selenium.webdriver.common.by import By
from behave import given, then
from time import sleep

COLOR_OPTIONS = (By.CSS_SELECTOR, '#variation_color_name li')
SELECTED_COLOR =(By.CSS_SELECTOR, '#variation_color_name span.selection')


@given('Open amazon jeans {productid} page')
def open_jeans_page(context, productid):
    context.driver.get(f'https://www.amazon.com/gp/product/{productid}/')


@then('Verify user can select through colors')
def verify_jeans_colors(context):
    expected_colors = ['Black', 'Blue Overdyed', 'Dark Vintage', 'Dark Wash', 'Indigo Wash', 'Light Vintage', 'Light Wash', 'Medium Vintage', 'Medium Wash', 'Rinse', 'Vintage Light Wash', 'Washed Black', 'Rinsed Vintage']
    colors = context.driver.find_elements(*COLOR_OPTIONS)
    print("Color element", colors)
    print("Color range ", range(len(colors)))

    for i in range(len(colors)):
        colors[i].click()
        sleep(1)
        color_text = context.driver.find_element(*SELECTED_COLOR).text
        assert color_text == expected_colors[i], f"color not match. Expected {expected_colors[i]} but got {color_text}"