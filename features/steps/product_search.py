from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC

# SEARCH_INPUT = (By.NAME, 'q')
SEARCH_SUBMIT = (By.NAME, 'btnK')
search_amz = (By.ID, 'twotabsearchtextbox')
seach_sub_amz = (By.CSS_SELECTOR, '#nav-search-submit-button')


@given('Open Google page')
def open_google(context):
    context.driver.get('https://www.google.com/')


@when('Input {search_word} into search field')
def input_search(context, search_word):
    search = context.driver.find_element(*search_amz)
    search.clear()
    search.send_keys(search_word)


@when('Click on search icon')
def click_search_icon(context):
    context.driver.find_element(*seach_sub_amz).click()


@when('Search for a {search_word} product')
def search_prod(context, search_word):
    context.app.header.search_amazon(search_word)

    '''search = context.driver.find_element(*search_amz)
    search.clear()
    search.send_keys(search_word)
    context.driver.find_element(*seach_sub_amz).click()'''


@then('Product results for {search_word} are shown')
def verify_found_results_text(context, search_word):
    assert search_word.lower() in context.driver.current_url.lower(), f"Expected query not in {context.driver.current_url.lower()}"
