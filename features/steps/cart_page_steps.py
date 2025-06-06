from selenium.webdriver.common.by import By
from behave import given, when, then


@then("Verify 'Your cart is empty' message is shown")
def verify_cart_empty(context):
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg']").text
    expected_text = 'Your cart is empty'
    assert actual_text == expected_text, f"Error, expected {expected_text} but got actual {actual_text}"