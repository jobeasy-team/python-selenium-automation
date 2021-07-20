from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys


@when('Search for Cologne')
def input_search(context):
    #context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('Cologne', Keys.RETURN)
    context.app.header.input_search('Cologne')
    context.app.header.click_search()


@when('Click on first product')
def click_prod(context):
    #context.driver.find_element(By.XPATH, "//div[@data-asin='B076BTZT9R']").click()
    context.app.product_item.click_on_item()


@when('Click on add to cart btn')
def add_item(context):
    context.driver.find_element(By.ID, "add-to-cart-button").click()


@then('Verify that cologne in your cart')
def verify_cart_count(context, expected_count):
    #actual_result = context.driver.find_element(By.CSS_SELECTOR,"div#huc-v2-order-row-messages").text
    #expected_result = "Added to Cart"
    #assert expected_result == actual_result, f'Expected{expected_result}, but got {actual_result}'
    context.app.header.verify_cart_count(expected_count)