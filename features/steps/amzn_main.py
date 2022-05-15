from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep

# I can come back and dlt this file or cstmr file after combining them later

search = (By.ID, 'twotabsearchtextbox')
cart_icon = (By.CSS_SELECTOR, 'div#nav-cart-count-container span.nav-cart-count.nav-cart-0')


@given('Open Amazon Main page')
def cart_btn(context):
    context.driver.get("https://www.amazon.com/")


@when('Click on the cart icon')
def cart_click(context):
    context.driver.find_element(*cart_icon).click()
    sleep(10)

