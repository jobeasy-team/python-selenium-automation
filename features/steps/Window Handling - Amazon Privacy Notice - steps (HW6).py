from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@given('Open Amazon T&C page')
def open_amazon_tc_page(context):
    context.driver.get(f'https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')


@when('Store original windows')
def store_original_window(context):
    context.original_window = context.driver.current_window_handle
    print(context.driver.window_handles)
    print('ORIGINAL WINDOW: ', context.original_window)


@when('Click on Amazon Privacy Notice link')
def click_amazon_privacy_link(context, ):
    context.driver.find_element(By.CSS_SELECTOR, "a[href='https://www.amazon.com/privacy']").click()


@when('Switch to the newly opened window')
def switch_to_new_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    All_our_handled_windows = context.driver.window_handles
    context.driver.switch_to.window(All_our_handled_windows[1]) #1: 2nd window that we switched to.


@then('Verify Amazon Privacy Notice page is opened')
def verify_privacy_notice_opened(context):
    expected_label = "Amazon.com Privacy Notice"
    actual_label = context.driver.find_element(By.CSS_SELECTOR, "h1").text
    assert actual_label == expected_label, f'Privacy Notice Label not found in page'


@then('User can close new window and switch back to original')
def close_and_switch_to_original(context):
    context.driver.switch_to.window(context.original_window)

