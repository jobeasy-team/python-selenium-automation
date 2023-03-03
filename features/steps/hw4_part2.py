from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

CART_BUTTON =  (By.CSS_SELECTOR, "#nav-cart-count")
FIRST_PRODUCT = (By.XPATH, "//span[text()='mens Performance Cotton Cushioned Athletic Ankle Socks']")

@when('Click on cart')
def click_search(context):
    #context.driver.find_element(By.CSS_SELECTOR, "#nav-cart-count").click()
    #sleep(2)
    context.driver.wait.until(EC.element_to_be_clickable(CART_BUTTON)).click()


@when('Click on first product')
def click_search(context):
    #context.driver.find_element(By.XPATH, "//span[text()='mens Performance Cotton Cushioned Athletic Ankle Socks']").click()
    #sleep(2)
    context.driver.wait.until(EC.element_to_be_clickable(FIRST_PRODUCT)).click()
@when('Click add to cart')
def click_search(context):
    context.driver.find_element(By.ID, "add-to-cart-button").click()

    #context.driver.wait.until(EC.element_to_be_clickable(SEARCH_SUBMIT))
