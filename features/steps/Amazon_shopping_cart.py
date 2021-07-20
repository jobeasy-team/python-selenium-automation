from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open Amazon homepage')
def open_amazon(context):
    #context.driver.get('https://www.amazon.com/')
    context.app.main_page.open_main()


@when('Click on shopping cart icon')
def click_icon(context):
    #context.driver.find_element(By. ID, 'nav-cart-count-container').click()
    context.app.header.click_icon()


@then('Verify Shopping cart is empty')
def verify_empty_cart(context):
    #actual_result = context.driver.find_element(By.CSS_SELECTOR, "h2.sc-your-amazon-cart-is-empty").text
    #expected_result = 'Your Amazon Cart is empty'
    #assert expected_result == actual_result, f'Expected {expected_result}, but got {actual_result}'
    context.app.shopping_cart.verify_empty_cart()
