from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys


@given ('Open Amazon Help Page')
def open_amazon_help(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')

@when ('Search for Cancel Order')
def search_cancel_order(context):
    context.driver.find_element(By.ID, 'helpsearch').send_keys('Cancel Order',Keys.ENTER)

@then ('Verify Cancel Items or Orders Text')
def verify_cancel_orders_text(context):
    actual_text = context.driver.find_element(By.XPATH, "//div[@class='help-content']/h1").text
    expected_text = 'Cancel Items or Orders'
    assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'


