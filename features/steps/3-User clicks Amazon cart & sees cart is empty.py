import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import given, when, then


#This step code below is included already within other step files.
#@given('User opens Amazon page (No Sign In)')
#def open_Amazon_NoSignIn(context):
#    context.driver.get('https://www.amazon.com')


@when('User clicks on Amazon cart')
def cart_button(context):
    context.driver.find_element(By.CSS_SELECTOR, '#nav-cart').click()


@then('cart results show {search_word}')
def verify_empty_cart(context, search_word):
    expected_header = "Your Amazon Cart is empty"
    actual_header = context.driver.find_element(By.CSS_SELECTOR, 'h2').text
    assert actual_header == expected_header, f'Verification error: {actual_header} did not match {expected_header}'


print("TEST CASE PASSED!")