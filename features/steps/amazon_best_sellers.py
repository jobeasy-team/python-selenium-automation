from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys

TOP_LINKS = (By.CSS_SELECTOR, '#zg_tabs a')
HEADER = (By.CSS_SELECTOR, '#zg_banner_text_wrapper')

@given('Open Amazon Best Sellers page')
def open_best_sellers_page(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers_8a080d3d7b55497ea1bdd97b7cff8b7b')

@then('Verify there are {expected_links} links')
def verify_bestseller_links(context, expected_links):
    actual_links = context.driver.find_elements(By.CSS_SELECTOR, 'div#zg_tabs li')
    assert int(expected_links) == len(actual_links), f'Expected {expected_links} links, but got {actual_links}'


@then('User can click through top links and verify correct page opens')
def click_through_top_links(context):
    top_links = context.driver.find_elements(*TOP_LINKS)
    for x in range(len(top_links)):
        link = context.driver.find_elements(*TOP_LINKS)[x]

        link_text = link.text
        link.click()

        header_text = context.driver.find_element(*HEADER).text
        assert link_text in header_text, f'Expected {link_text} not in {header_text}'