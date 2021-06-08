from selenium.webdriver.common.by import By
from behave import given, when, then

@when('Click Orders')
def click_orders(context):
    context.driver.find_element(By.ID, "nav-orders").click()

