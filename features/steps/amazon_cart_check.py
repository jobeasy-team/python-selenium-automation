from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys

@when('Click on cart')
def click_cart(context):
    context.driver.find_element(By.ID, 'nav-cart').click()

@then('Check that cart is Empty')
def verify_empty_cart(context):
    context.driver.find_element(By.ID, 'sc-empty-cart-message')

