from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep

empty = (By.CSS_SELECTOR, 'div.a-row.sc-your-amazon-cart-is-empty h2')
one_item = (By.CSS_SELECTOR, 'span.a-size-medium-plus.a-color-base.sw-atc-text.a-text-bold')


@then('Verify {expected_rslt}')
def cart_empty(context, expected_rslt):
    sleep(2)
    result = context.driver.find_element(*one_item)
    actual_rslt = result.text
    assert expected_rslt == actual_rslt, f'Error, Actual text {actual_rslt} does not match {expected_rslt}'
