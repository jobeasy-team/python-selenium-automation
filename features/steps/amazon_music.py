from behave import given, when, then
from selenium.webdriver.common.by import By


THREE_LINES = (By.CSS_SELECTOR, "i[class='hm-icon nav-sprite']")
MUSIC = (By.XPATH, "//a[@data-menu-id='3']")
NINE_ITEMS = (By.CSS_SELECTOR, "a[href*='nav_em__dm']")


@given("Open Amazon page music")
def open_music_page(context):
    context.driver.get('https://www.amazon.com/')


@when("Click on hamburger menu")
def hamburger_menu(context):
    menu = context.driver.find_element(*THREE_LINES)
    menu.click()


@then("Click on Amazon Music menu item")
def amazon_music(context):
    music = context.driver.find_element(*MUSIC)
    music.click()


@then("9 menu items are present")
def nine_items(context):
    items = context.driver.find_element(*NINE_ITEMS)
    items.click()
