from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

CART_EMPTY_MSG = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg'] h1")
PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='cartItem-title']")
TOTAL_TXT = (By.CSS_SELECTOR, "h2 [class*='styles_cart-summary-span']")


@then('Verify Cart Empty message is shown')
def verify_empty_cart_msg(context):
    expected_text = 'Your cart is empty'
    actual_text = context.driver.find_element(*CART_EMPTY_MSG).text
    assert actual_text == expected_text, f'Expected {expected_text} but got {actual_text}'


@when('Open cart page')
def open_cart(context):
    context.driver.get('https://www.target.com/cart')


@then('Verify cart has {amount} item(s)')
def verify_cart_items(context, amount):
    sleep(2)
    cart_summary = context.driver.find_element(*TOTAL_TXT).text
    assert f'{amount} item' in cart_summary, f"Expected {amount} items but got {cart_summary}"


@then('Verify product in cart is correct')
def verify_product(context):
    product_in_cart = context.driver.find_element(*PRODUCT_NAME).text
    print("Product in cart", product_in_cart)
    assert product_in_cart[:15] == context.product_name[:15], \
        f'Product in cart {product_in_cart}, but expected {context.product_name}'

