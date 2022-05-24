from behave import given, when, then
from selenium.webdriver.common.by import By


cncl_order = (By.XPATH, "//div[@class='help-content']/h1")


@then('Verify search results for {expected_rslt}')
def cancel_order(context, expected_rslt):
    actual_rslt = context.driver.find_element(*cncl_order)
    assert expected_rslt == actual_rslt, f'Error, Actual text {actual_rslt} does not match {expected_rslt}'


