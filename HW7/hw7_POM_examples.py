from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


@given('Open amazon page')
def open_amazon(context):
    # context.driver.get('https://www.amazon.com/')
    context.app.main_page.open_main()


@when('Click Amazon Orders link')
def click_ReturnsAndOrders(context):
    # context.driver.wait.until(EC.element_to_be_clickable(RETURNS_ORDERS), message="Button is not clickable").click()
    context.app.header.click_ReturnsAndOrders()


@then('Verify Sign In page is opened and text {expected_text} is displayed')
def verify_sign_in_page_displayed(context, expected_text):
    context.app.sign_in_page.verify_signin_text(expected_text)


# --------------------------------------------------------------------------------------------------

@when('Click on cart icon')
def click_cart_icon(context):
    context.app.header.click_cart_icon()


@then('Verify {expected_text} text present')
def verify_empty_cart(context, expected_text):
    context.app.cart_page.verify_cart_text(expected_text)


# -----------------------------------------------------------------------------------------------------
@when('Input text {search_word}')
def input_product_name(context, search_word):
    # context.driver.find_element(*AMAZON_SEARCH_FIELD).send_keys(search_word)
    context.app.header.input_search_text(search_word)


@when('Click on search button')
def click_search_button(context):
    # context.driver.find_element(*SEARCH_ICON).click()
    context.app.header.click_search()


@when('Click on the first product')
def click_first_product(context):
    # context.driver.find_element(*PRODUCT_PRICE).click()
    context.app.search_results_page.click_first_product()


@when('Click on Add to cart button')
def click_add_to_cart(context):
    context.app.product_page.click_add_to_cart()


@then('Verify cart has {expected_count} item(s)')
def verify_cart_count(context,expected_count):
    context.app.header.verify_cart_count(expected_count)
