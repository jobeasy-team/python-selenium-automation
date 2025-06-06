from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Search for {search_word}')
def search_product(context, search_word):
    context.driver.find_element(By.ID, 'search').send_keys(search_word)
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    sleep(5)


@when('Click on Cart icon')
def click_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartLink']").click()


@then('Verify header has {number} links')
def verify_header_links(context, number):
    print(type(number))
    links = context.driver.find_elements(By.CSS_SELECTOR, "[data-test*='@web/GlobalHeader/UtilityHeader/']")
    print(links)

    # 6 == 6
    assert len(links) == int(number), f'Expected {number} links but got {len(links)}'
