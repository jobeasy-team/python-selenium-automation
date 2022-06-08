from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

empty = (By.CSS_SELECTOR, 'div.a-row.sc-your-amazon-cart-is-empty h2')
one_item = (By.CSS_SELECTOR, 'span.a-size-medium-plus.a-color-base.sw-atc-text.a-text-bold')


@then('Verify {expected_rslt} text is present')
def cart_status(context, expected_rslt):
    #context.app.cart_page.cart_empty(expected_rslt)
    context.app.cart_page.cart_fill(expected_rslt)

    '''result = context.driver.find_element(*one_item)
    actual_rslt = result.text
    assert expected_rslt == actual_rslt, \
    f'Error, Actual text {actual_rslt} does not match {expected_rslt}'
    '''