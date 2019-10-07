from behave import then
from selenium.webdriver.common.by import By

EMAIL_FIELD = By.CSS_SELECTOR, "input[type='email']

@then('Verify Sign-in page is opened')
def verify_signin_opened(context):
    context.driver.find_element(*EMAIL_FIELD).click()
    assert 'https://www.amazon.com/ap/signin'in context.driver.current_url