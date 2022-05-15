from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep


@then("Click on Amazon's Choice")
def select_item(context):
    amzn_choice = (By.CSS_SELECTOR, 'div.a-section.a-spacing-base')
    context.driver.find_element(*amzn_choice).click()
