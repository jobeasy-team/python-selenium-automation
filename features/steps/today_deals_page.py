from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from behave import given, when, then

CURRENT_DEALS = (By.XPATH, "//div[contains(@class, 'faceoutTitle')]")
CHOSEN_PRODUCT = (By.XPATH, "//div[@id = '103_dealView_11']//child::span[@class='a-button-inner']")
CART_ITEM_COUNT = (By.XPATH, "//span[@id = 'nav-cart-count']")


@then("{expected_header} are shown")
def header_is_correct(context, expected_header):
    actual_header = context.driver.find_element(*CURRENT_DEALS).text
    assert expected_header in actual_header, f"Expected {expected_header}, but got {actual_header}"


@when("Select chosen gift and add to cart")
def chosen_gift(context):
    context.driver.find_element(*CHOSEN_PRODUCT).click()





