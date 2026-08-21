from selenium.webdriver.common.by import By
from behave import given, when, then

UTILITY_HEADER_WRAPPER = (By.CSS_SELECTOR, "[class*='utilityHeaderWrapper']")
UTILITY_HEADER_LINKS = (By.CSS_SELECTOR, "a[data-test*='@web/GlobalHeader/UtilityHeader']")
LISTINGS = (By.CSS_SELECTOR, "[data-test='@web/site-top-of-funnel/ProductCardWrapper']")
PRODUCT_IMG = (By.CSS_SELECTOR, 'img')
PRODUCT_TITLE = (By.CSS_SELECTOR, "[data-test='@web/ProductCard/title']")


@when('Search for {product}')
def search_product(context, product):
    context.app.header.search_product(product)


@when('Click on cart icon')
def click_cart(context):
    context.app.header.click_cart_icon()


@then('Verify Navigation Utility Header is shown')
def verify_utility_header(context):
    header_element = context.driver.find_element(*UTILITY_HEADER_WRAPPER)
    print(header_element)
    # context.driver.refresh()
    # header_element = context.driver.find_element(*UTILITY_HEADER_WRAPPER)
    # print(header_element)
    # header_element.click()


@then('Verify {expected_amount} Navigation Utility Header links are shown')
def verify_utility_header(context, expected_amount):
    expected_amount = int(expected_amount) # will need for asserting with len()
    header_links = context.driver.find_elements(*UTILITY_HEADER_LINKS)
    #  print(header_links)
    assert len(header_links) == expected_amount, f'Expected {expected_amount} links, but got {len(header_links)}'


@then('Verify that every product has a name and an image')
def verify_products_name_img(context):
    # To see ALL listings (comment out if you only check top ones):
    # context.driver.execute_script("window.scrollBy(0,2000)", "")
    # sleep(0.5)
    # context.driver.execute_script("window.scrollBy(0,2000)", "")
    # sleep(0.5)
    # If you ever need to scroll up, use negative numbers: context.driver.execute_script("window.scrollBy(0, -2000)", "")

    products = context.driver.find_elements(*LISTINGS)  # [WebEl1, WebEl2, WebEl3, WebEl4]
    for product in products[:8]:
        title = product.find_element(*PRODUCT_TITLE).text
        assert title, 'Product title not shown'
        print(f'🟢{title}')
        product.find_element(*PRODUCT_IMG)
