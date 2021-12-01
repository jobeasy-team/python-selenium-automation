from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver import Keys


@given('Open Amazon Customer help page')
def open_amazon(context):
    # open the url
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')


@when('Input cancel order in search field')
def input_word(context):
    search = context.driver.find_element(By.ID, 'helpsearch')
    search.clear()
    search.send_keys('cancel order')
    search.send_keys(Keys.RETURN)

@when('And Click Enter Key')
def click_enter(context):
    context.send_keys(Keys.RETURN)


@then('Product cancel order is shown on Amazon page')
def product_shown_on_page(context):
    context.driver.find_element(By.XPATH, "//b[contains(text(),'cancel order')]")


@then('Search Result has {expected_result} in it')
def verify_search_result(context, expected_result):

    result = context.driver.find_element(By.XPATH, "//b[contains(text(),'cancel order')]").text
    assert expected_result == result, f'error, actual {result} did not match {expected_result}'
    print('Test Passed')
    context.driver.quit()
