from selenium.webdriver.common.by import By
from behave import given, when, then


@when('Click Returns and Orders')
def click_orders(context):
    context.driver.find_element(By.ID, 'nav-orders').click()


@then('Verify that header {expected_result} is visible')
def verify_sign_in_header(context, expected_result):
    actual_result = context.driver.find_element(By.XPATH, "//h1[contains(text(), 'Sign in')]").text

    assert expected_result == actual_result, f'Expected {expected_result} but found actual {actual_result}'


@then('Verify that Email field is present')
def verify_email_field(context):
    actual_result = context.driver.find_element(By.ID, 'ap_email').is_displayed(), 'Email field not shown'



