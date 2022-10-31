from selenium.webdriver.common.by import By
from behave import when


ADD_CART=(By.ID, "add-to-cart-button")

@when('add to the cart')
def add_to_cart(context):
    context.driver.find_element(*ADD_CART).click()