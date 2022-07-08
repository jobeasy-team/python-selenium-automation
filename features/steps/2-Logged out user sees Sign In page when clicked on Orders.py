from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import given, when, then


@given('User opens Amazon(No Sign In)')
def open_Amazon_NoSignIn(context):
    context.driver.get('https://www.amazon.com')
# Note: Normally I would use this, but I have other files that clash with this so I kept it for note and use from other files.

#@when('User clicks on Orders')
#def click_Orders(context):
#    context.driver.find_element(By.XPATH, "//a[@id='nav-orders']")