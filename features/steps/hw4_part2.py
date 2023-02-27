from selenium.webdriver.common.by import By
from behave import given, when, then


@when('Click on cart')
def click_search(context):
    context.driver.find_element(By.CSS_SELECTOR, "#nav-cart-count").click()


@when('Click on first product')
def click_search(context):
    context.driver.find_element(By.XPATH, "//span[text()='mens Performance Cotton Cushioned Athletic Ankle Socks']").click()


@when('Click add to cart')
def click_search(context):
    context.driver.find_element(By.ID, "add-to-cart-button").click()
