from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('user is logged out')
def user_logged_out(context):
    actual_result = context.driver.find_element(By.CSS_SELECTOR, "span#nav-link-accountList-nav-line-1").text
    expected_result =("Hello, sign in")
    assert expected_result == actual_result, f"couldn't find {expected_result} lable, found :{actual_result} "


@when('click Returns & Orders link css')
def find_returns_orders(context):
    context.driver.find_element(By.CSS_SELECTOR, "a#nav-orders").click()

@then('Sign in page appears css')
def found_result(context):
    expected_result = "Sign in"
    actual_result = context.driver.find_element(By.CSS_SELECTOR, "h1.a-spacing-small").text
    assert expected_result == actual_result, f"Couldn't find {expected_result} , found :{actual_result} "
    email_input = context.driver.find_element(By.CSS_SELECTOR, "input#ap_email")
    print(email_input)
    assert email_input, f"Email input element is missing. "
    print('Test case passed')




