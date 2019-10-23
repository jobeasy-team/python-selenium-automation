from selenium.webdriver.common.by import By
from time import sleep
from behave import given, when, then

ORDERS_LINK = (By.CSS_SELECTOR, "a#nav-orders span.nav-line-2")
SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
SEARCH_ICON = (By.CSS_SELECTOR, "input.nav-input[type='submit']")
CUST_SERV_LINK = (By.LINK_TEXT, 'Customer Service')
SHOPPING_CART = (By.ID, 'nav-cart-count')


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com')
    sleep(1)


@given('Open Amazon page and maximize window')
def open_max_amazon(context):
    context.driver.get('https://www.amazon.com')
    context.driver.maximize_window()
    sleep(1)


@when('Click on Shopping Cart icon')
def click_cart_icon(context):
    context.driver.find_element(*SHOPPING_CART).click()
    sleep(1)


@when('Click on Orders link')
def click_orders_link(context):
    context.driver.find_element(*ORDERS_LINK).click()
    sleep(1)


@when('Search for {product}')
def search_product(context, product):
    search_field = context.driver.find_element(*SEARCH_INPUT)
    search_field.clear()
    search_field.send_keys(product)
    sleep(1.5)
    context.driver.find_element(*SEARCH_ICON).click()


@when('Click on Customer Service link')
def click_customer_service_link(context):
    context.driver.find_element(*CUST_SERV_LINK).click()


@then('Verify cart has {expected_item_count} item')
def verify_item_count(context, expected_item_count):
    sleep(1.5)
    actual_items = context.driver.find_element(By.ID, 'nav-cart-count').text
    assert actual_items == expected_item_count, f'Expected{expected_item_count}, but got{actual_items}'
