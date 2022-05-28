from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path='/Users/Adewale/OneDrive/Desktop/Automation Course/python-selenium-automation/chromedriver')
driver.wait = WebDriverWait(driver, 10)

@given('Open Amazon T&C page')
def open_amazon_privacy_page(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')


@when('Store original windows')
def store_window(context):
    context.original_window = context.driver.current_window_handle


@when('Click on Amazon Privacy Notice link')
def privacy_click(context):
    context.driver.find_element( By.LINK_TEXT,"Privacy Notice").click()


@when('Switch to the newly opened window')
def switch_to_new_window(context):
    WebDriverWait(driver, 10).until(EC.new_window_is_opened)
    print("\nAfter click: windows:", context.driver.window_handles)
    all_windows = context.driver.window_handles
    context.driver.switch_to.window(all_windows[1])


@then('Verify Amazon Privacy Notice page is opened')
def verify_privacy_page_opened(context):
    WebDriverWait(driver, 10).until(EC.new_window_is_opened)


@then('User can close new window and switch back to original')
def switch_back(context):
    context.driver.close()
    context.driver.switch_to.window(context.original_window)


