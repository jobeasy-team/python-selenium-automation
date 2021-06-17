from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Click on Amazon search icon')
def click_search(context):
    context.driver.find_element(By.ID, 'nav-search-submit-button').click()


@then('Verify search worked')
def verify_search_worked(context):
    actual_result = context.driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
    expected_result = '"Table"'
    assert expected_result == actual_result, f'Expected {expected_result}, but got {actual_result}'


@when('Click on the first product')
def click_first_product(context):
    context.driver.find_element(By.XPATH, '//div[@data-component-type="s-search-result"]//a[.//span[@class="a-price"]]').click()


@when('Click on Add to Cart button')
def click_add_to_cart_btn(context):
    context.driver.find_element(By.ID, 'add-to-cart-button').click()