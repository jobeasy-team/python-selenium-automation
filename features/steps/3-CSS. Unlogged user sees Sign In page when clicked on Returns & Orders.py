import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import given, when, then


@given('User opens Amazon page (No Sign In)')
def open_Amazon_NoSignIn(context):
    context.driver.get('https://www.amazon.com')


@when('User clicks on Returns & Orders')
def click_Returns_and_Orders(context):
    context.driver.find_element(By.CSS_SELECTOR, '#nav-orders').click()


@then('User sees Sign-In page')
def sign_in(context):
    expected_result = "Sign-In"
    actual_result = context.driver.find_element(By.CSS_SELECTOR, 'h1.a-spacing-small').text
    assert expected_result == actual_result,f'Expected {expected_result} but turned {actual_result}'


@then('Email input box is visible')
def email_input(context):
    context.driver.find_element(By.CSS_SELECTOR, '#ap_email').click()
#OR/AND (just in case)
    assert context.driver.find_element(By.ID, 'ap_email').is_displayed()

print('Test Case Passed.')
