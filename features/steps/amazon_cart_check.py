from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys

@when('Click on cart')
def click_cart(context):
    context.driver.find_element(By.ID, 'nav-cart').click()

@then('Check that cart is Empty')
def verify_empty_cart(context):
    context.driver.find_element(By.ID, 'sc-empty-cart-message')

@when('Search for {search_word}')
def search_for_product(context, search_word):
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys(search_word, Keys.ENTER)

@then('Verify cart has {expected_count} item')
def verify_cart_count(context, expected_count):
    items_in_cart = context.driver.find_element(By.ID, 'nav-cart-count').text
    assert items_in_cart == expected_count, f'Expected {expected_count}, but got {items_in_cart}'

