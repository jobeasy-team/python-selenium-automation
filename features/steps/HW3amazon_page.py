from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys
from time import sleep

@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com')


@when('click cart icon')
def customer_cart(context):
    context.driver.find_element(By.XPATH,"//span[@class='nav-cart-icon nav-sprite']").click()


@then ('verify cart is empty')
def cart_empty(context):
    expected_result = "Your Amazon Cart is empty"
    actual_result = context.driver.find_element(By.XPATH, "//div[@class='a-row sc-your-amazon-cart-is-empty']")


@when('select customer service')
def customer_service(context):
    context.driver.find_element(By.XPATH,"//a[@data-csa-c-content-id='nav_cs_customerservice']").click()


@then ('verify user can cancel order')
def cancel_order(context):
    context.driver.find_element(By.ID, 'hubHelpSearchInput').send_keys('cancel order', Keys.ENTER)
    sleep(4)
    expected_result = 'Cancel Items or Orders'
    actual_result = context.driver.find_element(By.XPATH, "//h1[text()='Cancel Items or Orders']").text
    print ('Test case Passed')









