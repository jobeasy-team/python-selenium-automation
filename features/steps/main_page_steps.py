from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from behave import given, when, then

ORDERS_LINK = (By.CSS_SELECTOR, "a#nav-orders span.nav-line-2")
SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
SEARCH_ICON = (By.CSS_SELECTOR, "input.nav-input[type='submit']")
CUST_SERV_LINK = (By.LINK_TEXT, 'Customer Service')
SHOPPING_CART = (By.ID, 'nav-cart-count')
HAM_MENU = (By.ID, 'nav-hamburger-menu')
AMAZON_MUSIC_MENU_ITEM = (By.XPATH, "//ul[contains(@class, 'hmenu-visible')]//div[contains(text(),'Amazon Music')]")
AMAZON_MUSIC_MENU_ITEM_RESULTS = (By.CSS_SELECTOR, "ul.hmenu-visible a:not(.hmenu-back-button)")
SIGN_IN_TOOLTIP = (By.ID, 'nav-signin-tooltip')
TODAY_DEALS_UNDER25 = (By.XPATH, "//a[contains(@aria-label, 'deals under $25')]")
CART_ITEM_COUNT = (By.XPATH, "//span[@id = 'nav-cart-count']")


@given('Open Amazon page')
def open_amazon(context):
    # context.driver.get('https://www.amazon.com')
    # sleep(1)
    context.app.main_page.open_page()


# @given('Open Amazon page and maximize window')
# def open_max_amazon(context):
#     context.driver.get('https://www.amazon.com')
#     context.driver.maximize_window()
#     sleep(1)


# StaleElementReferenceException explained:
# Message: stale element reference: element is not attached to the page document
# Web element changes ID after the REFRESHMENT and can not be found by the same ID (see console to compare)
# make sure to preform actions on element right before you communicate with the element
@when('Click on Shopping Cart icon')
def click_cart_icon(context):
    # cart_icon = context.driver.find_element(*SHOPPING_CART)
    # print(cart_icon)
    # context.driver.refresh()
    # cart_icon = context.driver.find_element(*SHOPPING_CART)
    # print(cart_icon)
    # cart_icon.click()
    # sleep(1)
    context.app.main_page.click_shopping_cart()


@when('Click on hamburger menu')
def click_ham_menu(context):
    # context.driver.find_element(*HAM_MENU).click()
    context.app.main_page.click_ham_menu()


@when('Click on Amazon Music menu item')
def click_amazon_music(context):
    context.app.side_menu.click_amazon_music()


@when('Click on Orders link')
def click_orders_link(context):
    context.app.main_page.click_orders_link()


@when('Search for {product}')
def search_product(context, product):
    # search_field = context.driver.find_element(*SEARCH_INPUT)
    # search_field.clear()
    # search_field.send_keys(product)
    # sleep(1.5)
    # context.driver.find_element(*SEARCH_ICON).click()
    context.app.main_page.search_for_keyword(product)


@when('Click on Customer Service link')
def click_customer_service_link(context):
    context.driver.find_element(*CUST_SERV_LINK).click()


@then('Verify cart has {expected_item_count} item')
def verify_item_count(context, expected_item_count):
    actual_item_count = context.driver.find_element(By.ID, 'nav-cart-count').text
    if int(actual_item_count) != 1:
        print(f"Cart has {actual_item_count} items")
    else:
        print(f"Cart has {actual_item_count} item")
    assert actual_item_count == expected_item_count, f'Expected{expected_item_count}, but got{actual_item_count}'


def expected_number_of_items(args):
    pass


@then("{expected_item_count} menu items are present")
def verify_amount_of_items(context, expected_item_count):
    # sleep(1)
    # actual_item_count = len(context.driver.find_elements(*AMAZON_MUSIC_MENU_ITEM_RESULTS))
    # assert actual_item_count == int(expected_item_count)
    # print(f"Expected {expected_item_count} items, "
    #             f"but got {actual_item_count}")
    expected_item_count = int(expected_item_count)
    context.app.side_menu.verify_amount_of_items(expected_item_count)


# =========================SignIn_Tooltip=========================================================
@then("Verify SignIn tooltip is present and clickable")
def verify_signin_tooltip_clickable(context):
    context.driver.wait.until(
        EC.element_to_be_clickable(SIGN_IN_TOOLTIP)
    )
    assert EC.element_to_be_clickable(SIGN_IN_TOOLTIP)


@when("Wait until SignIn tooltip disappears")
def signin_tooltip_disappears(context):
    context.driver.wait.until(
        EC.invisibility_of_element_located(SIGN_IN_TOOLTIP)
    )


@then("Verify SignIn tooltip is NOT clickable")
def verify_signin_tooltip_not_clickable(context):
    # wait UNTIL_NOT
    context.driver.wait.until_not(
        EC.element_to_be_clickable(SIGN_IN_TOOLTIP)
    )


# ======================Deals_under_$25===========================================================

@when("Store original windows")
def store_current_windows(context):
    context.original_window = context.driver.current_window_handle
    context.old_windows = context.driver.window_handles
    print('\noriginal window\n', context.original_window)
    print('\nold windows\n', context.old_windows)


@when("Click to open deals under 25 dollars")
def click_to_open_deals_under25(context):
    today_deals_u25 = context.driver.find_element(*TODAY_DEALS_UNDER25)
    today_deals_u25.click()


@when("Switch to the newly opened window")
def switch_to_new_window(context):
    context.driver.wait.until(EC.new_window_is_opened)

    current_windows = context.driver.window_handles
    print('\ncurrent windows\n', current_windows)
    # Switch to newly opened window
    # new_window = current_windows[1]
    # print('\nnew window\n', new_window)
    new_windows = current_windows
    for old_window in context.old_windows:
        new_windows.remove(old_window)

    print('\nnew windows\n', new_windows)

    # Switch to a freshly opened window
    context.driver.switch_to_window(new_windows[0])


@then("User can close new window and switch back to the original window")
def close_and_switch_window_back(context):
    # sleep(3)
    context.driver.close()
    # sleep(3)
    context.driver.switch_to_window(context.original_window)


@when("User can close new window and switch back to original and refresh main page")
def close_window_back_to_original_window(context):
    context.driver.close()
    context.driver.switch_to_window(context.original_window)
    context.driver.refresh()


@then("Verify cart contains {expected_num} item")
def verify_item_in_cart(context, expected_num):
    actual_num = context.driver.find_element(*CART_ITEM_COUNT).text
    assert expected_num in actual_num, f"Expected {expected_num},but got {actual_num} of items in the cart"


@when("Clicks on link to proceed to Best Seller page")
def best_seller_link_click(context):
    context.driver.find_element(By.LINK_TEXT, "Best Sellers").click()
