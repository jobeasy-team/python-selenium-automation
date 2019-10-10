from behave import given, when, then
from selenium.webdriver.common.by import By

ORDERS_LINK = (By.CSS_SELECTOR, "a#nav-orders span.nav-line-2")


@given('Open amazon page')
def open_amazon_page(context):
    context.driver.get('https://www.amazon.com/')


@when('Click on help button')
def click_on_help_button(context):
    context.driver.find_element(By.LINK_TEXT, 'Help').click()


@then('Find search field')
def input_cancel_order(context):
    search = context.driver.find_element(By.ID, "helpsearch")
    search.send_keys('Cancel orders')


@when('Input Dress into search field')
def search_dress(context):
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('dress')


@when('Click on search icon')
def click_search(context):
    context.driver.find_element(By.CSS_SELECTOR, "input.nav-input[type='submit']").click()

@when('Click on orders button')
def click_orders_link(context):
    context.driver.find_element(*ORDERS_LINK).click()
