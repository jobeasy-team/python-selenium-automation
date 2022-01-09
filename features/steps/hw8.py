from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from behave import given, when, then


@when('select department by baby')
def select_department(context):
    context.app.header.select_department()


@then('verify {category} department is selected')
def verify_department(context, category):
    context.app.search_result_page.verify_correct_department(category)