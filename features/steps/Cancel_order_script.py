from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys


@given('Open Amazon customer page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')



@when('Input Cancel order in search field and press enter to search')
def type_amazon(context):
    context.driver.find_element(By.ID, 'helpsearch').send_keys('Cancel Order', Keys.ENTER)



@then('Verify Cancel order text is shown')
def verify_search_worked(context):
    actual_text = context.driver.find_element(By.XPATH, "//div[@class='help-content']/h1").text
    expected_result = 'Cancel Items or Orders'
    assert expected_result == actual_text, f'Expected {expected_result}, but got {actual_text}'




