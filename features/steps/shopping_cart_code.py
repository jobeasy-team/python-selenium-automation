from behave import given, when, then
from selenium.webdriver.common.by import By


@given('Open amazon page')
def open_amazon_page(context):
    context.driver.get('https://www.amazon.com/')


@when('Click on shopping cart button')
def click_on_shopping_cart(context):
    context.driver.find_element(By.ID, 'nav-cart')


@then('Verify the cart is empty')
def verify_result(context):
    result_text = context.driver.find_element(By.XPATH, "//div[@class='a-row sc-cart-header']").text
    assert "Your Shopping Cart is empty." in result_text, f"Expected text is Your Shopping Cart is empty., but got {result_text}"


