from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# I can come back and dlt this file or cstmr file after combining them later

search = (By.ID, 'twotabsearchtextbox')
cart_icon = (By.CSS_SELECTOR, 'div#nav-cart-count-container span.nav-cart-count.nav-cart-0')
COLOR_OPT = (By.CSS_SELECTOR, 'ul[class*="imageSwa"] li[title*="Click to"]')
retOrders_btn = (By.CSS_SELECTOR, 'a[href*="order-history"]')


@given('Open Amazon Main page')
def open_amzn(context):
    context.app.main_page.open_main_pg()


@given('Open Amazon T&C page')
def terms_page(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html/ref'
                       '=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088 ')


# HW5
@given('Open Amazon {prod_id} product page')
def product_page(context, prod_id):
    context.driver.get(f'https://www.amazon.com/dp/{prod_id}/')


@when('Click on the cart icon')
def cart_click(context):
    context.app.header.cart_btn()
    '''context.driver.find_element(*cart_icon).click()
    context.driver.wait.until(EC.visibility_of_element_located(cart_icon))
'''


@when('Click Amazon Orders link')
def orders_click(context):
    context.app.header.orders_btn()


# HW8
@when('Select books department')
def select_dept(context):
    context.app.header.select_dept()


@then('Verify {dept} department is selected')
def correct_dept(context, dept):
    context.app.header.verify_dept()
