from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('User click on Returns and orders')
def click_ReturnsAndOrders(context):
    context.driver.find_element(By.ID, 'nav-orders').click()


@then('Verify that user sees Sign in page')
def display_SignIn(context):
    expected_text = context.driver.find_element(By.CSS_SELECTOR, 'h1.a-spacing-small').text
    print(expected_text)
    assert expected_text == 'Sign in', f'Text does not match'
