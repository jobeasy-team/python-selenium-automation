from selenium.webdriver.common.by import By
from behave import then

CART_SUBTOTAL_BOX = (By.CSS_SELECTOR, "div#huc-v2-order-row-inner div#hlb-subcart div.a-spacing-micro")
SHOP_CART = (By.ID, "sc-retail-cart-container")


@then('Verify that Your Shopping Cart is empty text is presented')
def verify_shop_cart(context):
    cart_results = context.driver.find_element(*SHOP_CART).text
    assert 'Your Shopping Cart is empty' in cart_results


@then('Verify {number_of_items} in the cart')
def item_in_the_cart(context, number_of_items):
    subtotal_item = context.driver.find_element(*CART_SUBTOTAL_BOX).text
    print('\n{}'.format(subtotal_item))
    assert number_of_items in subtotal_item, \
        f"Expected number of items '{number_of_items}', but got '{subtotal_item}'"
