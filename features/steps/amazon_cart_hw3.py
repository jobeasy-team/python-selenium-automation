from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('click cart icon')
def click_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "a#nav-cart").click()

@then('verify that the cart is empty')
def empty_cart(context):
    expected_result = "Your Amazon Cart is empty"
    actual_result = context.driver.find_element(By.CSS_SELECTOR, "div.sc-your-amazon-cart-is-empty").text
    assert expected_result == actual_result, f"couldn't find {expected_result} lable, found :{actual_result} lable"
