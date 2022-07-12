import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import given, when, then


@given('User opens Amazon(No Sign In)')
def open_Amazon_NoSignIn(context):
    context.driver.get('https://www.amazon.com')


@when('User clicks on Orders')
def click_Orders(context):
    context.driver.find_element(By.XPATH, "//a[@id='nav-orders']").click()


@then('User sees Sign In page')
def sign_in(context):
    expected_result = "Sign-In"
    actual_result = context.driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
    assert expected_result == actual_result,f'Expected {expected_result} but turned {actual_result}'


@then('email input is visible')
def email_input(context):
    context.driver.find_element(By.XPATH, "//input[@name='email']").click()


print('Test Case Passed.')






