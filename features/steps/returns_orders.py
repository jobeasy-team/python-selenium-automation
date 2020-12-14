from behave import given, when, then
from selenium.webdriver.common.by import By

BUTTON = (By.CSS_SELECTOR, "a[href='/gp/css/order-history?ref_=nav_orders_first']")
RESULT_PAGE = (By.CSS_SELECTOR, "h1[class='a-spacing-small']")


@given('Open Amazon page returns order')
def open_amazon_test(context):
    # context.driver.get('https://www.amazon.com/')
    context.app.main_page.open_amazon()


@when('Click Amazon Orders link returns order')
def click_button(context):
    # press_button = context.driver.find_element(*BUTTON)
    # press_button.click()
    # context.app.main_page.click_returns_orders()
    context.app.main_page.click_item(*BUTTON)


@then('Verify Sign text in the opened page returns order')
def verify_signin_page_text(context):
    # result = context.driver.find_element(*RESULT_PAGE)
    # print(f'got the value {result.text}')
    # assert result.text == 'Sign-In', f'Got Error Expected Sign-In, but got {result.text}'
    context.app.sign_in_page.verify_sign_in_page('Sign-In')
