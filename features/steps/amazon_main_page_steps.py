from selenium.webdriver.common.by import By
from behave import given, when, then


AMAZON_SEARCH_INPUT_FIELD = (By.ID, 'twotabsearchtextbox')
SEARCH_ICON = (By.ID, 'nav-search-submit-button')

@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Input text {search_word}')
def input_search_word(context, search_word):
    context.driver.find_element(*AMAZON_SEARCH_INPUT_FIELD).send_keys(search_word)


@when('Click on search button')
def click_search(context):
    context.driver.find_element(*SEARCH_ICON).click()

#
# @then('Verify that text {expected_result} is shown')
# def verify_search_result(context, expected_result):
#     actual_result = context.driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
#
#     assert expected_result == actual_result, f'Expected {expected_result} but got actual {actual_result}'

