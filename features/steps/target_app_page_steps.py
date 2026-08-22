from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@given('Open Target App page')
def open_target_app_page(context):
    context.app.target_app_page.open_target_app_page()


@when('Click Privacy Policy link')
def click_pp_link(context):
    context.app.target_app_page.click_pp_link()
    sleep(1)


@then('Verify Privacy Policy page opened')
def verify_pp_page_opened(context):
    context.app.privacy_page.verify_pp_page_opened()

