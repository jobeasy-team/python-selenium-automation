from behave import given, when, then
from selenium.webdriver.common.by import By


CART_ICON = (By.ID, 'nav-cart-text-container')
FOUND_TEXT = (By.XPATH, "//div[@class='a-row sc-your-amazon-cart-is-empty']")


@given('Open Amazon page shopping')
def open_shopping_page(context):
    # context.driver.get('https://www.amazon.com/')
    context.app.main_page.open_amazon()


@when('Click on cart icon shopping')
def click_cart_icon(context):
    # cart_icon = context.driver.find_element(*CART_ICON)
    # cart_icon.click()
    context.app.main_page.click_item(*CART_ICON)


@then('Verify Your Shopping Cart is empty text present shopping')
def verify_cart_text(context):
    # page = context.driver.find_element(*FOUND_TEXT)
    # assert page.text == 'Your Amazon Cart is empty', f'Got Error Expected Your Amazon Cart is empty, but got {page.text}'
    context.app.shopping_empty_page.verify_cart_empty('Your Amazon Cart is empty')