from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

PRIV_NOT = (By.CSS_SELECTOR, 'a[href="https://www.amazon.com/privacy"]')


@when('Store original windows')
def store_tcp(context):
    context.origin_wind = context.driver.current_window_handle
    print(context.origin_wind)
    print(context.driver.window_handles)


@when('Click on Amazon Privacy Notice link')
def clk_priv(context):
    context.driver.find_element(*PRIV_NOT).click()

