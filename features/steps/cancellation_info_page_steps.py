from selenium.webdriver.common.by import By
from behave import then

CANCELLATION_PAGE_INFO_RESULTS = (By.CSS_SELECTOR, "div.answer-box")


@then('Verify that Cancel Items or Orders text is presented')
def verify_cancel_items(context):
    box_result = context.driver.find_element(*CANCELLATION_PAGE_INFO_RESULTS).text
    assert 'Cancel Items or Orders' in box_result

