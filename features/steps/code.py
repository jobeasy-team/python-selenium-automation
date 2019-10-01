from selenium.webdriver.common.by import By
from behave import given, when, then

ORDERS_SUBMIT = (By.LINK_TEXT, 'Orders')
RESULT = (By.XPATH, "//div[@class = 'a-box-inner a-padding-extra-large']")


@given('Open amazon page')
def open_google(context):
    context.driver.get('https://www.amazon.com/')


@when('Click on orders button')
def click_order_icon(context):
    context.driver.find_element(*ORDERS_SUBMIT).click()


@then('Sign in page is shown')
def verify_result(context):
    context.driver.find_element(*RESULT)





