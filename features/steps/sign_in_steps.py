from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then


@then('Verify Sign In page opens')
def verify_signin_opened(context):
    context.driver.wait.until(EC.url_contains('https://www.amazon.com/ap/signin'))