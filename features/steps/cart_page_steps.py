from selenium.webdriver.common.by import By
from behave import given, when, then

CART = (By.ID, 'nav-cart-count')
PRODUCT_NAME = ()


@when('Open cart page')
def open_cart_page(context):
    context.driver.get('https://www.amazon.com/cart?ref_=ewc_gtc')


@then('Verify cart has {expected_count} item(s)')
def verify_cart_count(context, expected_count):
    actual_text = context.driver.find_element(*CART).text
    assert expected_count == actual_text, f'Expected {expected_count}, but got {actual_text} '