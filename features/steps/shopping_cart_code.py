from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep


@when('Click on shopping cart button')
def click_on_shopping_cart(context):
    context.driver.find_element(By.ID, 'nav-cart').click()


@then('Verify the cart is empty')
def verify_result(context):
    result = context.driver.find_element(By.XPATH, "//h1[@class = 'sc-empty-cart-header']").text
    assert "empty" in result, f"Expected text is empty, but got {result}"





