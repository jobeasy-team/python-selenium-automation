from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep

empty = (By.CSS_SELECTOR, "div.a-row h1.a-spacing-mini.a-spacing-top-base")


@then('Verify {expected_rslt}')
def cart_empty(context, expected_rslt):
    actual_rslt = context.driver.find_element(*empty)
    assert expected_rslt == actual_rslt, f'Error, Actual text {actual_rslt} does not match {expected_rslt}'
