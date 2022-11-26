from selenium.webdriver.common.by import By
from behave import when, then, given
from selenium.webdriver.support import expected_conditions as EC

Privacy_Notice=(By.CSS_SELECTOR, "a[href='https://www.amazon.com/privacy']")


@given("Open Amazon T&C page")
def open_TC_page(context):
    context.driver.get("https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088 ")


@when("store original windows")
def store_original(context):
    context.original_window= context.driver.current_window_handle
    print(context.original_window)


@when("click on Amazon Privacy Notice link")
def click_on_privacy_notice(context):
    context.driver.find_element(*Privacy_Notice).click()


@when("switch to the newly opened window")
def switch_to_new_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    current_window = context.driver.window_handles
    print(current_window)
    context.driver.switch_to.window(current_window[1])


@then("verify Amazon Privacy Notice is opened")
def privacy_notice_is_open(context):
    context.driver.wait.until(EC.url_contains('https://www.amazon.com/gp/help/customer/display.html?nodeId=GX7NJQ4ZB8MHFRNJ'))
    print(context.driver.current_window_handle)


@then("user can close new window and switch back to original")
def close_and_return_to_original(context):
    context.driver.close()
    context.driver.switch_to.window(context.original_window)




