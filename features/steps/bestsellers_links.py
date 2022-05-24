from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

links = (By.CSS_SELECTOR, 'div._p13n-zg-nav-tab-all_style_zg-tabs__EYPLq ul li ')


@given('Open Amazon BestSellers Page')
def cart_btn(context):
    context.driver.get("https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers")


@then('Verify there are {expected_amount} link')
def bs_links(context, expected_amount):
    expected_amount = int(expected_amount)
    LINKS = context.driver.find_elements(*links)
    context.driver.wait.until(EC.visibility_of_element_located(links))

    #verify, see lesson 5 video 1:13:32
    assert len(LINKS) == expected_amount, f'Expected {expected_amount} links but got {len(LINKS)}'
