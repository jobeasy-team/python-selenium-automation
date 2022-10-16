from selenium.webdriver.common.by import By
from behave import given, when, then

@then('user face with sign in page')
def sign_in_appeared(context):
    expected_value= 'Sign in'
    actual_value= context.driver.find_element(By.XPATH, "//h1[@class= 'a-spacing-small']").text
    assert expected_value== actual_value, f'error| Expected{expected_value}, but got {actual_value}'