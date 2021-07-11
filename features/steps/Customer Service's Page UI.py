from selenium.webdriver.common.by import By
from behave import given, when, then

@then('verify if user can see customer services page UI')
def verify_ui_elements(context):
    context.driver.find_elements(By.CSS_SELECTOR, "div.a-row")
