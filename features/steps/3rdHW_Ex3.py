from selenium.webdriver.common.by import By
from behave import given, when, then
@given('open Amazon website')
def open_amazon (context):
    context.driver.get('https://www.amazon.com/')


@when('user click on cart')
def Click_on_cart (context):
    context.driver.find_element(By.XPATH, "//span[@class= 'nav-cart-icon nav-sprite']").click


