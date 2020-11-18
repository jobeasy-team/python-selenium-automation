from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC


LINK = (By.XPATH, "//a[contains(text(), 'Amazon applications')]")
#STORE_NAME = (By.XPATH, "//td[@valign='top']")
STORE_NAME = (By.XPATH, "//td[@class='amabot_center']")


@given("Open Amazon T&C page")
def open_customer_service(context):
    context.driver.get("https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088")

@when("Click on Amazon applications link and store original window")
def click_link(context):
    context.original_windows = context.driver.window_handles
    context.original_window = context.driver.current_window_handle
    link = context.driver.find_element(*LINK)
    link.click()
    print(context.original_windows)
    print(context.original_window)

@when("Switch to the newly opened window")
def switch_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    new_windows = context.driver.window_handles
    print(new_windows)
    for window in context.original_windows:
        new_windows.remove(window)
    print(new_windows)
    context.driver.switch_to_window(new_windows[0])

@then('Amazon app page is opened')
def amazon_app_page(context):
    context.driver.find_element(*STORE_NAME)

@then('User can close new window and switch back to original')
def switch_back(context):
    context.driver.close()
    context.driver.switch_to_window(context.original_window)