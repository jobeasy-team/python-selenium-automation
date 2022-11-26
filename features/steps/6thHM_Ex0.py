from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, then, when
from time import sleep


SIGN_IN=(By.CSS_SELECTOR, (".span-action-inner"))

@when("open Amazon web page")
def open_amazon(context):
    context.driver.get("https://www.amazon.com/")

@then("verify sign in is clickable")
def verify_sign_in_clickable(context):
    context.driver.wait.until(EC.element_to_be_clickable(SIGN_IN), message= 'sing in not clickable yet')



@when("wait for {sec} seconds")
def wait_sec (context, sec):
    sleep(int(sec))

@then("Verify sign in disappears")
def sign_in_disapears (context):
    context.driver.wait.until(EC.invisibility_of_element_located(SIGN_IN))
