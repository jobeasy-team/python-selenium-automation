from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('user opens Amazon page')
def open_amazon_page(context):
    context.driver.get('https://www.amazon.com/')

@when('user clicks on cart icon')
def click_cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, '.nav-cart-icon').click()

@then('user sees empty cart message')
def verify_empty_cart(context):
    expected_result = 'Your Amazon Cart is empty'
    actual_result = context.driver.find_element(By.XPATH, "//h2[contains(text(), 'Your Amazon Cart is empty')]").text
    assert expected_result==actual_result, f"expected{expected_result} but got {actual_result}"



