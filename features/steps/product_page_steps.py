from selenium.webdriver.common.by import By
from time import sleep
from behave import given, when, then

ATC_BUTTON = (By.ID, 'add-to-cart-button')
CLOSING_X_SIDE_SECTION = (By.ID, 'attach-close_sideSheet-link')
COLOR_OPTIONS = (By. CSS_SELECTOR, 'div#variation_color_name li')
SELECTED_COLOR = (By.CSS_SELECTOR, 'div#variation_color_name span.selection')
COLOUR_VARIETY = (By.CSS_SELECTOR, "ul[data-action = 'a-button-group'] li")
SELECTED_COLOUR = (By.CSS_SELECTOR, "div span.selection")

@when('Click Add to cart button')
def click_add_to_cart(context):
    context.driver.find_element(*ATC_BUTTON).click()
    sleep(1.5)


@when('Close suggestion side section')
def close_side_suggestions(context):
    closing_btn = context.driver.find_elements(*CLOSING_X_SIDE_SECTION)
    if len(closing_btn) == 1:
        closing_btn[0].click()

@given('Open Amazon product {product_id} page')
def open_dress_page(context, product_id):
    context.driver.get(f"https://www.amazon.com/gp/product/{product_id}/")



@then('Verify User can select through colors')
def verify_colors(context):
    expected_colors = ['Black', 'Emerald', 'Ivory', 'Navy']

    color_web_elements = context.driver.find_elements(*COLOR_OPTIONS)
    print(color_web_elements)
    """for x in range(len(color_web_elements)):
        color_web_elements[x].click()
        actual_color = context.driver.find_element(*SELECTED_COLOR).text
        print(actual_color)
        assert actual_color == expected_colors[x], f"Expected color is {expected_colors[x]}, " \
                                                   f"but got {actual_color}"""""

    for color in color_web_elements:
        color.click()
        actual_color = context.driver.find_element(*SELECTED_COLOR).text
        print(actual_color)

        assert actual_color == expected_colors[color_web_elements.index(color)]


@then('Verify User can loop through colors')
def verify_colours(context):
    expected_colours = ['Medium Wash', 'Dark Wash', 'Rinse']
    colour_web_elements = context.driver.find_elements(*COLOUR_VARIETY)
    print(colour_web_elements)
    """for c in range(len(colour_web_elements)):
        colour_web_elements[c].click()
        actual_colour = context.driver.find_element(*SELECTED_COLOUR).text
        print(actual_colour)

        assert actual_colour == expected_colours[c], f"Expected colour is {expected_colours[c]}, " \
                                                     f"but got {actual_colour}"""""
    for colour in colour_web_elements:
        colour.click()
        sleep(3)
        actual_colour = context.driver.find_element(*SELECTED_COLOUR).text
        print(actual_colour)

        assert actual_colour == expected_colours[colour_web_elements.index(colour)]

