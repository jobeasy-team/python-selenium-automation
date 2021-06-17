from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys

@given('Open Amazon Best Sellers page')
def open_best_sellers_page(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')

@then('Verify there are {expected_links} links')
def verify_bestseller_links(context, expected_links):
    actual_links = context.driver.find_elements(By.CSS_SELECTOR, 'div#zg_tabs li')
    assert int(expected_links) == len(actual_links), f'Expected {expected_links} links, but got {actual_links}'