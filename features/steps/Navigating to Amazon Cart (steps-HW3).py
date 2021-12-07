from selenium.webdriver.common.by import By
from time import sleep
from behave import given, when, then


@given('Open Amazon website (No Sign In)')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/ref=nav_logo')


@when('Click on Amazon cart')
def enter_button(context):
    context.driver.find_element(By.CSS_SELECTOR, '#nav-cart-text-container').click()
    sleep(2)


@then('results for {search_word} is shown')
def verify_empty_cart_text(context, search_word):
    expected_header = "Your Amazon Cart is empty"
    actual_header = context.driver.find_element(By.CSS_SELECTOR, "h2").text
    assert actual_header == expected_header, f"ERROR, {actual_header} did not match {expected_header}"


print("TEST CASE PASSED!")
