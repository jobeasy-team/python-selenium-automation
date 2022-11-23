from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC

sign_in_popup = (By.CSS_SELECTOR, ".nav-action-inner")

@when('open Amazon web page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@then('verify sign in is clickable')
def signin_is_clickable(context):
    context.driver.wait.until(EC.element_to_be_clickable(sign_in_popup))

