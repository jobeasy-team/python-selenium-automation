from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from behave import given, when, then

CURRENT_DEALS = (By.XPATH, "//div[contains(@class, 'faceoutTitle')]")
CHOSEN_PRODUCT = (By.XPATH, "//div[@id='103_dealView_0']//div[@class='a-row layer backGround']")
CHOSEN_PRODUCT_DETAILS = (By.XPATH, "//li//img[@alt]")
CART_ITEM_COUNT = (By.XPATH, "//span[@id = 'nav-cart-count']")
ADD_TO_CART = (By.CSS_SELECTOR, "input#add-to-cart-button")


@then("{expected_header} are shown")
def header_is_correct(context, expected_header):
    actual_header = context.driver.find_element(*CURRENT_DEALS).text
    assert expected_header in actual_header, f"Expected {expected_header}, but got {actual_header}"


@when("Select chosen gift and add to cart")
def chosen_gift(context):
    context.driver.find_element(*CHOSEN_PRODUCT).click()
    sleep(1)
    context.driver.find_element(*CHOSEN_PRODUCT_DETAILS).click()
    sleep(1)
    context.driver.find_element(*ADD_TO_CART).click()
    sleep(1)
