from selenium.webdriver.common.by import By
from time import sleep
from behave import given, when, then

ATC_BUTTON = (By.ID, 'add-to-cart-button')
CLOSING_X_SIDE_SECTION = (By.ID, 'attach-close_sideSheet-link')


@when('Click Add to cart button')
def click_add_to_cart(context):
    context.driver.find_element(*ATC_BUTTON).click()
    sleep(1.5)


@when('Close suggestion side section')
def close_side_suggestions(context):
    closing_btn = context.driver.find_elements(*CLOSING_X_SIDE_SECTION)
    if len(closing_btn) == 1:
        closing_btn[0].click()



