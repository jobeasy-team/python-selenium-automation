from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys
from time import sleep

@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com')


@when('customer searches for marcy multi-purpose adjustable workout utility weight bench')
def customer_search(context):
    context.driver.find_element(By.ID,"twotabsearchtextbox").send_keys('marcy multi-purpose adjustable workout utility weight bench',Keys.ENTER)


@then ('lamp is added to cart')
def lamp_add(context):
    context.driver.find_element(By.XPATH,"//div[@data-component-type='s-impression-logger']//a[.//span[@class='a-price']]").click()
    context.driver.find_element(By.ID, "add-to-cart-button").click()


@then ('verify cart has{expected_result} item added')
def product_shown(context, expected_result):

    actual_result = context.driver.find_element(By.ID, 'nav-cart-count').text
    assert int(expected_result) == int(actual_result), f'expected {expected_result} got {actual_result}'
    print ('Test Case Passed')
















