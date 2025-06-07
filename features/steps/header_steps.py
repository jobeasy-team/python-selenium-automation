from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


SEARCH_FIELD = (By.ID, 'search')
SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
HEADER_LINKS = (By.CSS_SELECTOR, "[data-test*='@web/GlobalHeader/UtilityHeader/']")


@when('Search for {search_word}')
def search_product(context, search_word):
    context.driver.find_element(*SEARCH_FIELD).send_keys(search_word)
    context.driver.find_element(*SEARCH_BTN).click()
    sleep(10)


@when('Click on Cart icon')
def click_cart(context):
    context.driver.find_element(*CART_ICON).click()


@then('Verify header has {number} links')
def verify_header_links(context, number):
    print(type(number))
    links = context.driver.find_elements(*HEADER_LINKS)
    print(links)

    # 6 == 6
    assert len(links) == int(number), f'Expected {number} links but got {len(links)}'
