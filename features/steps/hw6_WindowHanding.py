from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from behave import given, when, then


@given('Open the Amazon {some} page')
def open_amazon(context, some):
    context.driver.get(f'https://www.amazon.com/{some}')


@when('Store original window')
def store_window(context):
    context.original_window = context.driver.current_window_handle
    print('original window', context.original_window)


@when('Click on Amazon Privacy Notice link')
def click_amazon_privacy_notice_link(context):
    context.driver.find_element(By.XPATH, "//a[@href='https://www.amazon.com/privacy']").click()


@when('Switch to the newly opened window')
def switch_to_newly_opened_window(context):
    # WebDriverWait(context.driver, 10).until(EC.new_window_is_opened)
    context.driver.wait.until(EC.new_window_is_opened)
    print(context.driver.current_window_handle)
    windows = context.driver.window_handles
    context.driver.switch_to.window(windows[1])


@then('Verify Amazon Privacy Notice page is opened')
def verify_amazon_privacy_notice_page_is_open(context):
    assert 'https://www.amazon.com/gp/help/customer/display.html' in context.driver.current_url, f'Blog page not open'


@then('User can close new window and switch back to original')
def verify_close_new_window_switch_back_to_original(context):
    context.driver.close()
    context.driver.switch_to.window(context.original_window)
