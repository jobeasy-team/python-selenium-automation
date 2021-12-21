
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from behave import given, when, then


@given('Open Amazon help page')
def open_amazon_help(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')


@when('Input {search_word} into search library')
def input_search(context, search_word):
    context.driver.find_element(By.ID, 'helpsearch').send_keys('cancel order')


@when('Begin search')
def enter_button(context):
    context.driver.find_element(By.ID, 'helpsearch').send_keys(Keys.RETURN)


@then('results for {search_word} are shown')
def verify_text_results(context, search_word):
    expected_header = "Cancel Items or Orders"
    actual_header = context.driver.find_element(By.XPATH, "//div/h1").text
    assert actual_header == expected_header, f"ERROR, {actual_header} did not match {expected_header}"


print("TEST CASE PASSED!")
