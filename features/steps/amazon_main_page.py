from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open product page')
def open_product_page(context):
    context.app.main_page.open_product_page()



@given('Open Amazon page')
def open_amazon(context):
   # context.driver.get('https://www.amazon.com/')
    context.app.main_page.open_page()


@when('Click Amazon Orders link')
def click_amazon_orders(context):
    context.app.header.click_amazon_orders()

@when('Click on cart icon')
def click_on_cart_icon(context):
    context.app.header.click_on_cart_icon()


@when('Select baby department')
def select_dept(context):
    context.app.header.select_dept()

@when('Search for {search_word}')
def search_amazon(context, search_word):
    context.app.header.search_amazon(search_word)

@when('Hover over new arrivals')
def hover_new_arrivals(context):
    context.app.header.hover_new_arrivals()

@when ('Hover over language options')
def hover_lang(context):
    context.app.header.hover_lang()


@then('verify Spanish Option present')
def verify_spanish_lang(context):
    context.app.header.verify_spanish_lang()

@then('verify new arrivals present')
def verify_new_arrivals(context):
    context.app.header.verify_new_arrivals()

@then('verify baby department is selected')
def verify_department(context):
    context.app.header.verify_department()


@then('Verify Sign in page is opened')
def verify_signin_page(context):
    context.app.header.verify_signin_page()

@then('Verify "Your Shopping Cart is Empty" text is present')
def verify_cart_empty(context):
    context.app.header.verify_cart_empty()
