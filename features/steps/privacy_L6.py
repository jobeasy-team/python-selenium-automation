from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

priv_pg_txt = (By.CSS_SELECTOR, 'h1')


@when('Switch to the newly opened window')
def switch_win(context):
    context.driver.wait.until(EC.new_window_is_opened)
    print('/After, click windows:', context.driver.window_handles)
    all_windows = context.driver.window_handles
    context.driver.switch_to.window(all_windows[1])


@then('Verify Amazon Privacy Notice page is opened')
def ver_priv_txt(context):
    context.driver.wait.until(EC.url_contains('GX7NJQ4ZB8MHFRNJ'))
    context.driver.find_element(*priv_pg_txt).text


@then('User can close new window')
def close_win(context):
    context.driver.close()


@then('switch back to original')
def return_to_origin(context):
    context.driver.switch_to.window(context.origin_wind)

