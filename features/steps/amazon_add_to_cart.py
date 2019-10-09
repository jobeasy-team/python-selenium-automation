from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open amazon page')
def open_google(context):
    context.driver.get('https://www.amazon.com/')


@when('Input Dress into search field')
def search_dress(context):
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('dress')


sleep(4)


@when('Click on search icon')
def click_search(context):
    context.driver.find_element(By.CSS_SELECTOR, "input.nav-input[type='submit']").click()


@then('Product result for dress is shown')
def verify_result(context):
    result_text = context.driver.find_element(By.CSS_SELECTOR, "h1 span.a-text-bold").text
    assert "dress" in result_text


@when('Click on dress')
def click_dress(context):
    context.driver.find_element(By.PARTIAL_LINK_TEXT, 'BELONGSCI Women').click()


@then('Click on add in cart')
def click_add_cart(context):
    context.driver.find_element(By.NAME, 'submit.add-to-cart').click()


@when('Click on cart icon')
def click_cart_icon(context):
    context.driver.find_element(By.ID, 'nav-cart').click()


@then('Verify the item is in cart')
def verify_item(context):
    verify_cart = context.driver.find_element(By.ID, 'sc-subtotal-label-activecart').text
    assert 'item' in verify_cart





