from selenium.webdriver.common.by import By
from time import sleep
from behave import given, when

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
    context.driver.find_element(*SEARCH_ICON).click()


@when('Click on Customer Service link')
def click_customer_service_link(context):
    context.driver.find_element(*CUST_SERV_LINK).click()
