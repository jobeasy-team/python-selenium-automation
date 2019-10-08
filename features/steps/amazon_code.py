from behave import given, when, then
from selenium.webdriver.common.by import By


@given('Open amazon page')
def open_amazon_page(context):
    context.driver.get('https://www.amazon.com/')


@when('Click on hamburger menu')
def click_hamburger_menu(context):
    context.driver.find_element(By.ID, "nav-hamburger-menu").click()


@when('Click on help button')
def click_on_help(context):
    context.driver.find_element(By.LINK_TEXT, "Help").click()


@then('Input cancel orders in search field')
def input_text_in_search(context):
    context.driver.find_element(By.XPATH, "//input[@class = 'a-input-text a-span12']").send_keys("Cancel orders")


@then('Click go button')
def click_go_button(context):
    context.driver.find_element(By.XPATH, "//input[@class = 'a-button-input']").click()


@then('Verify cancel order text')
def verify_text(context):
    context.driver.find_element("//a[@class = 'a-link-normal']").text()


@when("Click hamburger menu")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When Click hamburger menu')