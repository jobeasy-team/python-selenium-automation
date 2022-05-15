from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep

empty = (By.CSS_SELECTOR, 'div.a-row.sc-your-amazon-cart-is-empty h2')


@then('Verify {expected_rslt}')
def cart_empty(context, expected_rslt):
    sleep(2)
    result = context.driver.find_element(*empty)
    actual_rslt = result.text
    assert expected_rslt == actual_rslt, f'Error, Actual text {actual_rslt} does not match {expected_rslt}'
