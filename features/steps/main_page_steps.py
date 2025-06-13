from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target main page')
def open_main(context):
    # context.driver.get('https://www.target.com/')
    context.app.main_page.open_main_page()