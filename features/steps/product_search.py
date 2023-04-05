from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

SEARCH_INPUT = (By.CSS_SELECTOR, '#twotabsearchtextbox')
SEARCH_SUBMIT = (By.CSS_SELECTOR, '#nav-search-submit-button')


@given('Open Google page')
def open_google(context):
    context.driver.get('https://www.google.com/')


@when('Input {search_word} into search field')
def input_search(context, search_word):
    search = context.driver.find_element(*SEARCH_INPUT)
    search.clear()
    search.send_keys(search_word)
    sleep(4)
    #context.driver.wait.until(EC.element_to_be_clickable())


@when('Input text {search_word}')
def input_search_text(context, search_word):
    search = context.driver.find_element(*SEARCH_INPUT)
    search.send_keys(search_word)




@when('Click on search icon')
def click_search_icon(context):
    context.driver.find_element(*SEARCH_SUBMIT).click()
    sleep(1)
    #context.driver.wait.until(EC.element_to_be_clickable(SEARCH_SUBMIT))





@then('Product results for {search_word} are shown')
def verify_found_results_text(context, search_word):
    assert search_word.lower() in context.driver.current_url.lower(), f"Expected query not in {context.driver.current_url.lower()}"


@then('Verify {category} department is selected')
def verify_selected_dept(context, category):
    context.app.product_search_page.verify_selected_dept(category)
