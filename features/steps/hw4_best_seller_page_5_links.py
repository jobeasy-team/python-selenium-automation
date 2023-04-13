from selenium.webdriver.common.by import By
from behave import given, when, then


SUBHEADER_LINKS = (By.CSS_SELECTOR, "#zg_header li")


@given('Open best seller page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')


@then('Verify that subheader has {expected_amount} links')
def verify_header_link_count(context, expected_amount):
    expected_amount = int(expected_amount)
    header_links = context.driver.find_elements(*SUBHEADER_LINKS)
    assert len(header_links) == expected_amount, f'Expected {expected_amount} links but got {len(header_links)}'