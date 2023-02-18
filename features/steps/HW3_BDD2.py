from selenium.webdriver.common.by import By
from behave import given, when, then


@when('User click on cart icon')
def click_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, 'a[href="/gp/cart/view.html?ref_=nav_cart"]').click()

@then('Verify that Amazon cart is empty')
def verify_cart(context):
    str = context.driver.find_element(By.CSS_SELECTOR, 'div.a-column.a-span8.a-span-last h2').text
    print(str)
    assert str == 'Your Amazon Cart is empty', f"Cart is not empty"
