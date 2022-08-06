from selenium.webdriver.common.by import By
from behave import when, then
from time import sleep

RESULT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")
PRODUCT_PRICE = (By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a-price']]")
SEARCH_RESULTS = (By.CSS_SELECTOR, "[data-component-type='s-search-result']")
PRODUCT_TITLE = (By.CSS_SELECTOR, 'h2 span.a-text-normal')
PRODUCT_IMG = (By.CSS_SELECTOR, ".s-image[data-image-latency='s-product-image']")


@when('Click on the first product')
def click_first_product(context):
    context.driver.find_element(*PRODUCT_PRICE).click()


@then('User sees results for {expected_result}')
def verify_search_results(context, expected_result):
    context.app.search_results_page.verify_search_results(expected_result)

