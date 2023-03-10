from selenium.webdriver.common.by import By
from behave import given, then


TOP_LINKS = (By.CSS_SELECTOR, '#zg_header a')
HEADER = (By.CSS_SELECTOR, '#zg_banner_text')


@given('Open Amazon Bestsellers')
def open_amazon_bestsellers(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')


@then('User can click through top links and verify correct page opens')
def click_thru_top(context):
    top_links = context.driver.find_elements(*TOP_LINKS)  # [WebEl1,WebEl2, WebEl3,... ]

    for i in range(len(top_links)):  # for x from 0 to 4
        link_to_click = context.driver.find_elements(*TOP_LINKS)[i] # 2
        link_text = link_to_click.text
        print(link_text)

        link_to_click.click()

        header_text = context.driver.find_element(*HEADER).text
        print(header_text)
        assert link_text in header_text, f'Expected {link_text} to be in {header_text}'


