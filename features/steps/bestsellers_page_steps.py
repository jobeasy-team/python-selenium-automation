from behave import given, then
from selenium.webdriver.common.by import By
from time import sleep

TOP_LINKS = (By.CSS_SELECTOR, '#zg_header a')
HEADER = (By.CSS_SELECTOR, '#zg_banner_text')


@given('Open Amazon Bestsellers')
def open_amazon_bestsellers(context):
    # context.driver.get('https://www.amazon.com/gp/bestsellers/')
    context.app.bestsellers_page.open_bestsellers()


@then('Verify there are {expected_links} links')
def verify_links_count(context, expected_links):
    # actual_links = context.driver.find_elements(*TOP_LINKS)
    # assert len(actual_links) == int(expected_links), f' Expected {expected_links} links, but got {len(actual_links)}'
    context.app.bestsellers_page.verify_links_preset(expected_links)


@then('User can click through top links and verify correct page opens')
def click_thru_top(context):
    top_links = context.driver.find_elements(*TOP_LINKS)  # [WebEl1,WebEl2, WebEl3,... ]

    for x in range(len(top_links)):  # From 0 to 4 # 0
        link_to_click = context.driver.find_elements(*TOP_LINKS)[x] # 0
        link_text = link_to_click.text
        link_to_click.click()
        sleep(1)
        header_text = context.driver.find_element(*HEADER).text
        assert link_text in header_text, f'Expected {link_text} to be in {header_text}'
