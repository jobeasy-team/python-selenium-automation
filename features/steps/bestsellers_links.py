from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep

links = (By.CSS_SELECTOR, 'div._p13n-zg-nav-tab-all_style_zg-tabs__EYPLq ul li ')


@given('Open Amazon BestSellers Page')
def cart_btn(context):
    context.driver.get("https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers")
    sleep(2)


@then('Verify there are {expected_amount} link')
def bs_links(context, expected_amount):
    expected_amount = int(expected_amount)
    LINKS = context.driver.find_elements(*links)

    assert len(LINKS) == expected_amount, f'Expected {expected_amount} links but got {len(LINKS)}'
