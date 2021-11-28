from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open Amazon page')
def open_google(context):
    context.driver.get('https://www.amazon.com/')
    context.driver.find_element(By.xpath, "")
