from selenium.webdriver.common.by import By
from behave import given, when, then





@given('Open Amazon page')
def open_amazon(context):
   # context.driver.get('https://www.amazon.com/')
    context.app.main_page.open_main_page()


@when('Click Amazon Orders link')
def click_amazon(context):
    context.app.base_page.click()

