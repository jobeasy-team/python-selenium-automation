from selenium.webdriver.common.by import By
from time import sleep
from behave import then

EMAIL_FIELD = (By.CSS_SELECTOR, "input[type='email']")


@then('Verify Sign in page opened')
def verify_sign_in_open(context):
    # context.app.sign_in_page.open_page(self.url = "/ap/signin")
    # # assert 'https://www.amazon.com/ap/signin' in context.driver.current_url
    # sleep(2)
    context.app.sign_in_page.verify_url('/ap/signin')
