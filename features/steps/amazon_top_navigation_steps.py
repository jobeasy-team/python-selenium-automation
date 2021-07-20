from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Click Orders')
def click_orders(context):
    #context.driver.find_element(By.ID, 'nav-orders').click()
    context.app.header.click_orders()


@when('move mouse over flag icon')
def hoover_flag_icon(context):
    context.app.header.hoover_flag_icon()


@when('Select Health, Household & Baby care')
def select_department(context):
    context.app.header.select_department()


@then('Spanish language selection is visible')
def verify_spanish_lang_present(context):
    context.app.header.verify_spanish_lang_present()


@when('Move mouser over to New Arrivals tab')
def hoover_tab(context):
    context.app.clothing_header.hoover_tab()


@then('Verify if that user can see deals')
def verify_women_section(context):
    context.app.clothing_header.verify_women_section()