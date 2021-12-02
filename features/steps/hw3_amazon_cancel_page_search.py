from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver import Keys


@given('Open Amazon Customer help page')
def open_amazon(context):
    # open the url
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')


@when('Input {search_txt} in search field')
def input_word(context, search_txt):
    search = context.driver.find_element(By.ID, 'helpsearch')
    search.clear()
    search.send_keys(search_txt)
    search.send_keys(Keys.RETURN)

@when('And Click Enter Key')
def click_enter(context):
    context.send_keys(Keys.RETURN)


@then('Product {search_txt} is shown on Amazon page')
def product_shown_on_page(context, search_txt):
    context.driver.find_element(By.XPATH, f"//b[contains(text(), '{search_txt}')]")


@then('Search Result has {expected_result} in it')
def verify_search_result(context, expected_result):
    result = context.driver.find_element(By.XPATH, f"//b[contains(text(),'{expected_result}')]").text
    assert expected_result == result, f'error, actual {result} did not match {expected_result}'
    print('Test Passed')
    context.driver.quit()
