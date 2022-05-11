from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from behave import given, when, then


@given('open Amazon help search')
def open_amazon_help(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')


@when('Input Cancel order')
def search_amazon_help(context):
    context.driver.find_element('Cancel order')


@when('click ENTER')
def click_enter(context):
    search = context.driver.find_element(By.ID, 'helpsearch')
    search.clear()
    search.send_keys('Cancel order', Keys.ENTER)


SEARCH_RESULT_TEXT = (By.XPATH, "//div[contains(@class, 'help-cont')]/h1")


@then('Verify that results for "Cancel Items or Orders" are shown')
def verify_search(context):
    actual_result = context.driver.find_element(*SEARCH_RESULT_TEXT).text
    assert expected_result == actual_result, f'Error! Actual result {actual_result} does not match expected result {expected_result}'



