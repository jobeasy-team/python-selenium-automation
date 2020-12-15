from behave import given, when, then
from selenium.webdriver.common.by import By


THREE_LINES = (By.CSS_SELECTOR, "i[class='hm-icon nav-sprite']")
MUSIC = (By.XPATH, "//a[@data-menu-id='3']")
#NINE_ITEMS = (By.CSS_SELECTOR, "a[href*='nav_em__dm']")
NINE_ITEMS = (By.CSS_SELECTOR, "ul.hmenu-translateX a[class=hmenu-item]")


@given("Open Amazon page music")
def open_music_page(context):
    # context.driver.get('https://www.amazon.com/')
    context.app.main_page.open_amazon()


@when("Click on hamburger menu")
def hamburger_menu(context):
    # menu = context.driver.find_element(*THREE_LINES)
    # menu.click()
    context.app.main_page.click_item(*THREE_LINES)


@then("Click on Amazon Music menu item")
def amazon_music(context):
    # music = context.driver.find_element(*MUSIC)
    # music.click()
    context.app.hamburger_menu_page.click_menu_item(*MUSIC)


@then("9 menu items are present")
def nine_items(context):
    context.app.hamburger_menu_page.verify_links(9, *NINE_ITEMS)
