from behave import given, when, then
from selenium.webdriver.common.by import By


@given('Open amazon page')
def open_amazon_page(context):
    context.driver.get('https://www.amazon.com/')


@when('Click on help button')
def click_on_help_button(context):
    context.driver.find_element(By.LINK_TEXT, 'Help').click()


@then('Find search field')
def input_cancel_order(context):
    search = context.driver.find_element(By.ID, "helpsearch")
    search.send_keys('Cancel orders')


@then('Click go button')
def click_go(context):
    context.driver.find_element(By.XPATH,"//input[@class = 'a-button-input']").click()


@then('Verify cancel items or orders text is present')
def verify_result(context):
    result_text = context.driver.find_element(By.XPATH, "//div[@class='help-content']/h1").text
    assert "cancel orders" in result_text, f"Expected cancel orders or items in text, but got{result_text}"
















