from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

ORDERS_BTN = (By.ID, 'nav-orders')
INPUT_FIELD = (By.ID, 'twotabsearchtextbox')
SEARCH_ICON = (By.ID, 'nav-search-submit-button')
HAM_MENU = (By.ID, 'nav-hamburger-menu')
FOOTER_LINKS = (By.CSS_SELECTOR, 'table.navFooterMoreOnAmazon td a')
SIGN_IN_POPUP_BTN = (By.CSS_SELECTOR, '#nav-signin-tooltip span.nav-action-inner')


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Search for {search_word} on amazon')
def search_product(context, search_word):
    context.driver.find_element(*INPUT_FIELD).send_keys(search_word)
    context.driver.find_element(*SEARCH_ICON).click()
    sleep(1)


@when('Click Orders')
def click_orders(context):
    context.driver.find_element(*ORDERS_BTN).click()


@when('Click on button from SignIn popup')
def click_sign_in_btn(context):
    context.driver.wait.until(
        EC.element_to_be_clickable(SIGN_IN_POPUP_BTN), message='SignIn not clickable'
    ).click()


@then('Verify hamburger menu is present')
def verify_hamburger_menu_present(context):
    context.driver.find_element(*HAM_MENU)


@then('Verify {expected_amount} footer links are shown')
def verify_footer_links_present(context, expected_amount):
    expected_amount = int(expected_amount)  # '38' => 38
    links = context.driver.find_elements(*FOOTER_LINKS)

    assert len(links) == expected_amount, \
        f'Expected {expected_amount} links but got {len(links)}'
