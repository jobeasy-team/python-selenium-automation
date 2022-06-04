from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


SIN_BTN = (By.CSS_SELECTOR, '#nav-flyout-ya-signin .nav-action-inner')



@when('click on button from signin popup')
def click_sign_in_btn(context):
   signin = context.driver.wait.until(
       EC.element_to_be_clickable(SIN_BTN), 'signin button not clickable'
   )
   signin.click()




@then('verify sign in page is opened')
def verify_sign_in_page(context):
    context.driver.wait.until(EC.url_contains('https://www.amazon.com/ap/signin?openid.pape.max_auth_age'),
                              message='sign in never opened')
    expected_result = 'sign in page must come'
    actual_result = context.driver.get(f"https://www.amazon.com/ap/signin?")

    assert expected_result == actual_result,  f'Error! Actual text {actual_result} does not match expected{expected_result}'




