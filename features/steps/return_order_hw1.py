from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('open amazon home page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com')

@when('click Returns & Orders link')
def find_returns_orders(context):
    context.driver.find_element(By.XPATH, "//a[@id='nav-orders']").click()

@then('Sign in page appears')
def found_result(context):
    expected_result = "Sign on"
    actual_result = context.driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
    assert expected_result == actual_result, f"couldn't find {expected_result} lable, found :{actual_result} lable"
    email_input = context.driver.find_element(By.XPATH, "//input[@id='ap_email']")
    print(email_input)
    assert email_input, f"Email input element is missing. "
    print('Test case passed')




