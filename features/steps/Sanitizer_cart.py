from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys


@when('Search for Sanitizer')
def input_search(context):
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('Sanitizer', Keys.RETURN)

@when('Click on first item')
def click_item(context):
    context.driver.find_element(By.XPATH, "//h2[contains(@class, 'a-size-mini a-spacing-none a-color-base s-line-clamp-4')]").click()

@when('Click on add to cart button')
def add_item(context):
    context.driver.find_element(By.ID, "add-to-cart-button").click()

@then('Verify that sanitizer in your shopping cart')
def verify_item(context):
    actual_result = context.driver.find_element(By.CSS_SELECTOR,"div#huc-v2-order-row-messages").text
    expected_result = "Added to Cart"
    assert expected_result == actual_result, f'Expected{expected_result}, but got {actual_result}'



