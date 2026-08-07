from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open main target page')
def open_target_main(context):
    context.driver.get('https://www.target.com/')


@when('Search for tea')
def search_product(context):
    context.driver.find_element(By.ID, 'search').send_keys('tea')
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']").click()
    sleep(7)


@then('Verify search results are shown for tea')
def verify_search_result_shown(context):
    expected_text = 'tea'
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "[data-test='lp-resultsCount']").text
    assert expected_text in actual_text, f'Expected text {expected_text} not in actual {actual_text}'
