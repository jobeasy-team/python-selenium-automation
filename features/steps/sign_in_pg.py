from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


@then('Verify {exp_res} page is opened')
def opened_sign_in(context, exp_res):
    context.app.sign_in_page.ver_sign_in_page(exp_res)

