from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_FIELD = (By.ID, 'search')
SEARCH_BTN = (By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']")
CART_ICON = (By.CSS_SELECTOR, "a[data-test='@web/CartLink']")
UTILITY_HEADER_WRAPPER = (By.CSS_SELECTOR, "[class*='utilityHeaderWrapper']")
UTILITY_HEADER_LINKS = (By.CSS_SELECTOR, "a[data-test*='@web/GlobalHeader/UtilityHeader']")


@when('Search for {product}')
def search_product(context, product):
    context.driver.find_element(*SEARCH_FIELD).send_keys(product)
    context.driver.find_element(*SEARCH_BTN).click()
    sleep(10)


@when('Click on cart icon')
def click_cart(context):
    context.driver.find_element(*CART_ICON).click()


@then('Verify Navigation Utility Header is shown')
def verify_utility_header(context):
    context.driver.find_element(*UTILITY_HEADER_WRAPPER)


@then('Verify {expected_amount} Navigation Utility Header links are shown')
def verify_utility_header(context, expected_amount):
    expected_amount = int(expected_amount) # will need for asserting with len()
    header_links = context.driver.find_elements(*UTILITY_HEADER_LINKS)
    #  print(header_links)
    assert len(header_links) == expected_amount, f'Expected {expected_amount} links, but got {len(header_links)}'