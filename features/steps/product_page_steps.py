from selenium.webdriver.common.by import By
from time import sleep
from behave import given, when, then

ATC_BUTTON = (By.ID, 'add-to-cart-button')
@when('Click Add to cart button')
def click_add_to_cart(context):
    context.driver.find_element(*ATC_BUTTON).click()