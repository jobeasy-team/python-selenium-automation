from behave import given, when, then
from selenium.webdriver.common.by import By

SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
SEARCH_ICON = (By.XPATH, "//input[@value='Go']")
SEARCH_RESULT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")


@given('Open Amazon page1')
def open_amazon(context):
    print("I am in open")
    # context.driver.get('https://www.amazon.com/')
    context.app.main_page.open_amazon()


@when('Input Dress into Amazon search field1')
def input_search_word(context):
    # context.driver.find_element(*SEARCH_INPUT).send_keys('Dress')
    context.app.main_page.input_search_word('Dress')


@when('Click on Amazon search icon1')
def click_search_icon(context):
    # search_icon = context.driver.find_element(*SEARCH_ICON)
    # search_icon.click()
    context.app.main_page.click_search_icon()


@then('search result Dress is shown1')
def verify_search_result(context):
    # result = context.driver.find_element(*SEARCH_RESULT)
    # assert result.text == '"Dress"', f'Error.Expected Dress, but got {result.text}'
    context.app.search_results_page.verify_search_result('"Dress"')
