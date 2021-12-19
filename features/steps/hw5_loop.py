from time import sleep

from selenium.webdriver.common.by import By
from behave import given, then

colors_array = (By.CSS_SELECTOR, '#variation_color_name li')
selected_color = (By.CSS_SELECTOR, '#variation_color_name .selection')

sales_items = (By.CSS_SELECTOR, '#wfm-pmd_deals_section li a-section div.a-text-left')
sales_itme_regular_text = (By.CSS_SELECTOR, 'span.wfm-sales-item-card__regular-price')
product_name = (By.CSS_SELECTOR, 'span.wfm-sales-item-card__product-name')


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


@given('Open Amazon {some} page')
def open_amazon(context, some):
    context.driver.get(f'https://www.amazon.com/{some}')
    context.driver.find_element(By.CSS_SELECTOR, 'span.glow-toaster-button-dismiss input').click()


@then('verify every product has a text {target} and product name')
def verify_every_product_with_name_and_regular_label(context, target):
    for item in context.driver.find_elements(*sales_items):
        actual_text = item.find_element(*sales_itme_regular_text).text
        assert target in actual_text, f'Expected {target}, but it shows {actual_text}'
        actual_name = item.find_element(*product_name).text
        assert actual_name != "", f' Expected name, but shows nothing'

