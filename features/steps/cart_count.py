from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep



CART_ITEM_NUM = (By.ID, 'nav-cart-count-container')


@when('open cart page')
def open_cart_page(context):
    context.driver.get('https://www.amazon.com/gp/cart/view.html?ref_=nav_cart')




@then('verify cart has {expected_count} item(s)')
def verify_cart_count(context, expected_count):
    actual_text = context.driver.find_element(*CART_ITEM_NUM).text
    assert expected_count == actual_text, f'Expected {expected_count},but got {actual_text}'
