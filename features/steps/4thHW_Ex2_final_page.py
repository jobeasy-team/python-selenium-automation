from selenium.webdriver.common.by import By
from behave import then


CART_TEXT=(By.CSS_SELECTOR, ".a-size-medium-plus a-color-base sw-atc-text a-text-bold")
CART_NUMBER= (By.ID, "nav-cart-count")

@then('verify there is one item')
def verify_add_to_cart(context):
    # expected_text='Added to Cart'
    expected_number='1'
    # actual_text= context.driver.find_element(*CART_TEXT).text
    actual_number= context.driver.find_element(*CART_NUMBER).text
    assert expected_number==actual_number , f'Expected {expected_number} but it shows {actual_number}'

