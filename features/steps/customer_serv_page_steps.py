from selenium.webdriver.common.by import By
from behave import when
from time import sleep

CANCEL_ORDER_INPUT = (By.ID, 'helpsearch')
CLICK_BUTTON = (By.ID, 'helpSearchSubmit')


@when('Input Cancel order into search box')
def input_cancelling(context):
    cancel_input = context.driver.find_element(*CANCEL_ORDER_INPUT)
    cancel_input.clear()
    cancel_input.send_keys('Cancel order')
    sleep(3)

@when('Click Go button')
def click_go(context):
    context.driver.find_element(By.ID, 'helpSearchSubmit').click()
