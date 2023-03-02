from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC

RETURNS_ORDERS = (By.ID, 'nav-orders')
TEXT = (By.CSS_SELECTOR, 'h1.a-spacing-small')
@given('Open amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('User click on Returns and orders')
def click_ReturnsAndOrders(context):
    context.driver.wait.until(EC.element_to_be_clickable(RETURNS_ORDERS)).click()


@then('Verify that user sees Sign in page')
def display_SignIn(context):
    expected_text = context.driver.wait.until(EC.presence_of_element_located(TEXT)).text
    print(expected_text)
    assert expected_text == 'Sign in', f'Text does not match'
