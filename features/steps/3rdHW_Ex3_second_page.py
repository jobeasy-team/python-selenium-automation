from selenium.webdriver.common.by import By
from behave import given, when, then


@then ('text to show cart is empty')
def show_cart_empty (context):
    expected_value= 'Your Amazon Cart is empty-'
    actual_value= context.driver.find_element(By.XPATH,"//div[@class='a-row sc-your-amazon-cart-is-empty").text
    assert expected_value==actual_value , f'error| Expected{expected_value}, but got {actual_value}'
