from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open Amazon Bestseller page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/Best-Sellers/zgbs/')


@then('Verify if user can see 5 links on the page')
def verify_link_displayed(context):
    links = context.driver.find_elements(By.CSS_SELECTOR, "#zg_tabs a")
    print(links)
    assert len(links) == 5, f'Expected 5 links, but got {len(links)}'


