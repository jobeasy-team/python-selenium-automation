from selenium.webdriver.common.by import By
from behave import given, when, then


TOP_LINKS = (By. CSS_SELECTOR, "div#zg_tabs a")
HEADER = (By.CSS_SELECTOR, "div#zg_banner_text_wrapper")


@given('Open Amazon Bestseller page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/Best-Sellers/zgbs/')


@then('Verify if user can see 5 links on the page')
def verify_link_displayed(context):
    links = context.driver.find_elements(By.CSS_SELECTOR, "#zg_tabs a")
    print(links)
    assert len(links) == 5, f'Expected 5 links, but got {len(links)}'



@then('Verify if user can click through headers links')
def click_through_links(context):
    top_links = context.driver.find_elements(*TOP_LINKS)

    for x in range(len(top_links)):
        link = context.driver.find_elements(*TOP_LINKS)[x]

        link_text = link.text
        link.click()

        header_text = context.driver.find_element(*HEADER).text
        assert link_text in header_text, f'Expected {link_text} not {header_text}'

