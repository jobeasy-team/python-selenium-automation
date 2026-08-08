from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

RESULTS_COUNT_TXT = (By.CSS_SELECTOR, "[data-test='lp-resultsCount']")


@then('Verify search results are shown for {expected_product}')
def verify_search_result_shown(context, expected_product):
    actual_text = context.driver.find_element(*RESULTS_COUNT_TXT).text
    assert expected_product in actual_text, f'Expected text {expected_product} not in actual {actual_text}'
