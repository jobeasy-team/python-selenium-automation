from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from behave import when, given, then
from time import sleep


ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')
PRODUCT_NAME = (By.ID, 'productTitle')
PRODUCT_PRICE = (By.ID, 'corePrice_feature_div')

COLOR_OPTIONS = (By.CSS_SELECTOR, "#variation_color_name li")
CURRENT_COLOR = (By.CSS_SELECTOR, "#variation_color_name .selection")

THUMBNAIL_IMG = (By.CSS_SELECTOR, '#altImages input.a-button-input')

@given('Open hat product on Amazon')
def open_google(context):
    context.driver.get('https://www.amazon.com/EEYON-Baseball-Adjustable-Unstructured-Women-Grey/dp/B09ZQV36QJ/ref=sr_1_45?crid=1DC496ODTRCD5&keywords=hat&qid=1677867360&sprefix=hat%2Caps%2C179&sr=8-45')


# @given('Open Amazon product {product_id} page')
# def open_product(context, product_id):
#     context.driver.get(f'https://www.amazon.com/{product_id}/')


@when('Click on Add to cart button')
def click_add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()
    sleep(4)


@when('Store product name and price')
def get_product_name(context):
    context.product_name = context.driver.find_element(*PRODUCT_NAME).text
    print(f'Current product: {context.product_name}')
    context.product_price = context.driver.find_element(*PRODUCT_PRICE).text
    print(f'Current product price: {context.product_price}')


@then('Verify user can click through colors')
def verify_user_can_select_colors(context):
    context.driver.find_element(*COLOR_OPTIONS).click() # click on 1

    all_color_options = context.driver.find_elements(*COLOR_OPTIONS)
    print('All colors:', all_color_options)
    expected_colors = all_color_options

    actual_colors = []
    for color in all_color_options:
        color.click()
        current_color = context.driver.find_element(*CURRENT_COLOR).text
        print('Current color: ', current_color)
        actual_colors += [current_color]

    #assert expected_colors == actual_colors, f'Expected {expected_colors}, but got {actual_colors}'

    # Example with THUMBNAIL_IMG:
    # all_imgs = context.driver.find_elements(*THUMBNAIL_IMG)
    #
    # for img in all_imgs:
    #     img.click()