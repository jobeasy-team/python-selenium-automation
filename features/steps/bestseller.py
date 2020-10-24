from behave import given, then
from selenium.webdriver.common.by import By


@given('Open amazon bestsellers')
def open_page(context):
    context .driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')


@then('Verify 5 links')
def verify_links(context):
    link = len(context.driver.find_elements(By.CSS_SELECTOR, "a[href*='ref=zg_bs_tab']"))
    assert link == 5, f'Error. Expected 5, but got {link}'