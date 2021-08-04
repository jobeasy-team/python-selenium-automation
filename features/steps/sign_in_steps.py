from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep


@when('Wait for {sec_count} seconds')
def sleep_sec(context, sec_count):
    sleep(int(sec_count))

@then('Verify Sign in page opened')
def verify_sign_in_opened(context):
    assert 'https://www.amazon.com/ap/signin' in context.driver.current_url, f'Wrong url {context.driver.current_url}'


@then('Verify Sign in popup is clickable')
def verify_sign_in_popup_clickable(context):
    context.driver.WebDriverWait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#nav-signin-tooltip .nav-action-inner')))


@then('Verify Sign in popup disappears')
def verify_signin_popup_disappears(context):
    pass


