from selenium.webdriver.common.by import By
from behave import given, when, then


@when('Click Amazon Orders link')
def click_amazon_orders_link(context):
    context.app.main_page.click_order()


@when('Click on Cart Icon')
def click_on_cart_icon(context):
     context.app.main_page.click_cart()


@then('Verify Sign In page is opened')
def verify_page_is_open(context):
    context.app.signin_page.verify_url_contains_signin()


@then('Verify {expect_text} text present')
def verify_text_present(context, expect_text):
    context.app.cart_page.verify_text_present(expect_text)
