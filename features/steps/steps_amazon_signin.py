from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Click on orders')
def click_search(context):
    context.driver.find_element(By.XPATH, "//span[text()='& Orders']").click()


@then('Verify that text {expected_result} is shown')
def verify_search_result(context, expected_result):
    actual_result = context.driver.find_element(By.CSS_SELECTOR, "div.sc-cart-header").text
    assert expected_result == actual_result, f'Expected {expected_result} but got actual {actual_result}'


