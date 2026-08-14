from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

RESULTS_COUNT_TXT = (By.CSS_SELECTOR, "[data-test='lp-resultsCount']")
ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
SIDE_NAV_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")
SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")


@when('Click on Add to Cart button')
def click_add_to_cart(context):
    # context.driver.find_elements(*ADD_TO_CART_BTN)[0].click()
    context.driver.find_element(*ADD_TO_CART_BTN).click()  # always clicks on 1st Add to cart btn


@when('Store product name')
def store_product_name(context):
    # sleep(2)
    # context.product_name = context.driver.find_element(*SIDE_NAV_PRODUCT_NAME).text
    context.wait.until(
        EC.element_to_be_clickable(SIDE_NAV_ADD_TO_CART_BTN),
        message=f'Add to cart btn not clickable')

    context.product_name = context.wait.until(
        EC.visibility_of_element_located(SIDE_NAV_PRODUCT_NAME),
        message=f'Product name not visible by {SIDE_NAV_PRODUCT_NAME}'
    ).text

    print("Product:", context.product_name)


@when('Confirm Add to Cart button from side navigation')
def side_nav_click_add_to_cart(context):
    context.driver.find_element(*SIDE_NAV_ADD_TO_CART_BTN).click()
    sleep(2)


@then('Verify search results are shown for {expected_product}')
def verify_search_result_shown(context, expected_product):
    actual_text = context.driver.find_element(*RESULTS_COUNT_TXT).text
    assert expected_product in actual_text, f'Expected text {expected_product} not in actual {actual_text}'
