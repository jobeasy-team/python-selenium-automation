from selenium.webdriver.common.by import By
from behave import then
from selenium.webdriver.support import expected_conditions as EC


@then('Verify Sign in page opened')
def verify_sign_in_opened(context):
    context.driver.wait.until(EC.url_contains('ap/signin'), message='Signin URL did not open')