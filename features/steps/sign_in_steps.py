from selenium.webdriver.common.by import By
from behave import given, when, then


@then('Verify Sign in page opened')
def verify_sign_in_opened(context):
    assert 'https://www.amazon.com/ap/signin' in context.driver.current_url, f'Wrong url {context.driver.current_url}'