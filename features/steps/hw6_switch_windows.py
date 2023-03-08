from multiprocessing import context

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import  sleep

PRIVACY_LINK = (By. XPATH, '//a[@href="https://www.amazon.com/privacy"]')


@given('Open conditions page')
def open_conditions_page(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')


@given('Store original window')
def store_current_window(context):
    context.original_window = context.driver.current_window_handle
    print(context.original_window)


@when('Click on privacy link')
def click_privacy_link(context):
    context.driver.find_element(*PRIVACY_LINK).click()
    sleep(5)


@when('Switch to new window')
def switch_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    windows = context.driver.window_handles
    print('\nAll Windows: ', windows)
    context.driver.switch_to.window(windows[1])

    context.current_window = context.driver.current_window_handle
    print('\nAfter we switched:')
    print(context.current_window)


@then('Verify privacy page is open')
def verify_privacy_page_opened(context):
    context.driver.wait.until(EC.url_contains('https://www.amazon.com/gp/help/customer/display.'))


@then('Close privacy page')
def close_privacy_page(context):
    context.driver.close()

@then('Return to original window')
def switch_to_original(context):
    context.driver.switch_to.window(context.original_window)