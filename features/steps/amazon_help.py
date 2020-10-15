from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from behave import given, when, then
from time import sleep


@given("Open amazon help search page")
def open_amazon (context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')


@when('Input cancel order in Search the help library')
def input_search_word(context):
    search = context.driver.find_element(By.ID, 'helpsearch').send_keys('Cancel order',Keys.ENTER)

@then('click enter')
def click_search_icon(context):
    search_icon = context.driver.find_element(By.ID, 'helpsearch').send_keys('Cancel order',Keys.ENTER)

@then('Verify Cancel Items or Orders text present')
def verify_search_result(context):
    result = context.driver.find_element(By.XPATH, "//h1[text()='Cancel Items or Orders']")
    assert result.text == 'Cancel Items or Orders', f'Error.Expected Cancel Items or Orders , but got {result.text}'