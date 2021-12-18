from selenium.webdriver.common.by import By
from selenium import webdriver
from behave import given, when, then


@given('Open Amazon bestSeller page')
def open_amazon(context):
    # open the url
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')


@then('bestseller page is shown')
def best_seller_shown(context):
    result_obj = context.driver.find_element(By.CSS_SELECTOR, "#zg_banner_text")
    assert result_obj.text == "Amazon Best Sellers", f"Error, didn't open best sellers page, but {result_obj.text} page"


@then('{number_links} links display on the page')
def links_display(context, number_links):
    link_array = context.driver.find_elements(By.CSS_SELECTOR, "._p13n-zg-nav-tab-all_style_zg-tabs__EYPLq li")
    assert len(link_array) == int(number_links), f"Error, number of links is not {number_links}, but {len(link_array)}"
    print('Test Passed')


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Search for {search_item}')
def search(context, search_item):
    context.driver.find_element(By.ID, "twotabsearchtextbox").send_keys(search_item)


@when('Click for search icon')
def click_search_button(context):
    context.driver.find_element(By.ID, "nav-search-submit-button").click()


@when('Click on the first product')
def click_first_prod(context):
    context.driver.find_element(By.CSS_SELECTOR, "span.a-price-whole").click()


@when('Click on Add to cart button')
def click_add_cart_button(context):
    context.driver.find_element(By.ID, "add-to-cart-button").click()


@when('Open cart page')
def open_cart(context):
    context.driver.find_element(By.ID, "nav-cart-count").click()


@then('Verify cart has {number} item(s)')
def verify_cart_item(context, number):
    cart_item_no = context.driver.find_element(By.ID, "nav-cart-count").text
    assert int(cart_item_no) == int(number), f"error, real number is {cart_item_no}, not {number}"


@given('pen Amazon Customer Service Page')
def open_customer_service_page(context):
    context.driver.get("https://www.amazon.com/gp/help/customer/display.html")
