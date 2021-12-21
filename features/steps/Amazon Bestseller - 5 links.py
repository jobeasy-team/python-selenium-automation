from selenium.webdriver.common.by import By
from time import sleep
from behave import given, when, then


fivelinks=(By.CSS_SELECTOR, "#zg_header a")


@when('Click on Bestsellers')
def bestseller_click(context):
    context.driver.find_element(By.CSS_SELECTOR, "a.nav-a[href*='/gp/bestsellers/']").click()


@then('Verify {expected_count} links')
def verify_fivelinks(context, expected_count):
    expected_count= int(expected_count)
    fivelinks_count= len(context.driver.find_elements(*fivelinks))
    assert expected_count == fivelinks_count,f'Expected {expected_count} but turned {fivelinks_count}'

