from behave import given, when, then
from selenium.webdriver.common.by import By


@then('Add item to cart')
def add_to_cart(context):
    one_time = (By.CSS_SELECTOR, 'div a i.a-icon.a-accordion-radio.a-icon-radio-inactive')
    context.driver.find_element(*one_time).click()
    context.driver.find_element(By.ID, 'add-to-cart-button').click()
