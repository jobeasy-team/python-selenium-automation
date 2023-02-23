from selenium.webdriver.common.by import By
from behave import given, when, then

OPEN_BESTSELLERS_PAGE = (By.CSS_SELECTOR, 'a[href*="ref_=nav_cs_bestsellers"]')
BESTSELLERS_LINKS = (By.CSS_SELECTOR, 'div._p13n-zg-nav-tab-all_style_zg-tabs__EYPLq ul li')


@when('click on Best Sellers tab')
def open_bestsellers_page(context):
    context.driver.find_element(*OPEN_BESTSELLERS_PAGE).click()


@then('Verify the number of links are {expected_amount}')
def verify_number_of_links(context, expected_amount):
    expected_amount = int(expected_amount)
    links = context.driver.find_elements(*BESTSELLERS_LINKS)
    assert expected_amount == len(links), f'Expected {expected_amount} and actual are {links}'
