from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions

@given('Open Amazon T&C page')
def open_terms_and_conditions_page(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')

@when('Store original windows')
def store_original_windows(context):
    original_url = 'https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088'

# @when('Click on Amazon Privacy Notice link')
# def click_amazon_privacy_notice(context):
