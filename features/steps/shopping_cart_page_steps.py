from selenium.webdriver.common.by import By
from behave import then

SHOP_CART = (By.ID, "sc-retail-cart-container")
@then('Verify that Your Shopping Cart is empty text is presented')
def verify_shop_cart(context):
    cart_results = context.driver.find_element(*SHOP_CART).text
    assert 'Your Shopping Cart is empty' in cart_results
