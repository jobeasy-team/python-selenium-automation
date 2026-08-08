from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open main target page')
def open_target_main(context):
    context.driver.get('https://www.target.com/')
