from behave import given, when, then
from selenium.webdriver.common.by import By


@given('Open amazon page')
def open_amazon_page(context):
    context.driver.get('https://www.amazon.com/')


@when('Click on menu')
def click_menu(context):
    context.driver.find_element(By.XPATH, "//li[@class = 'nav_last']").click()


@when('Click on help button')
def click_on_help(context):
    context.driver.find_element(By.LINK_TEXT, "Help").click()


@then('Input cancel orders in search field')
def input_text_in_search(context):
    context.driver.find_element(By.XPATH, "//input[@class = 'a-input-text a-span12']").send_keys("Cancel orders")


@then('Click go button')
def click_go_button(context):
    context.driver.find_element(By.XPATH, "//input[@class = 'a-button-input']").click()


@then('Verify cancel order text is present')
def verify_text_is_present(context):
    context.driver.find_element(By.XPATH, "//div[@class ='help-content']/h1")

