from selenium.webdriver.common.by import By
from time import sleep
from behave import then

EMAIL_FIELD = (By.CSS_SELECTOR, "input[type='email']")


@then('Verify Sign in page opened')
def verify_signin__open(context):
    context.driver.find_element(*EMAIL_FIELD)
    assert 'https://www.amazon.com/ap/signin' in context.driver.current_url
    sleep(2)
