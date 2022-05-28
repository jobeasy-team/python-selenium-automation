from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys



COLOR_OPTIONS = (By.CSS_SELECTOR, "li[id*='color_name']")
COLOR_NAME = (By.XPATH, "//span[@class='selection']")


@given('Open Amazon product page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/gp/product/B07BJKRR25/')


@then('Verify user can click through colors')
def color_select(context):
    expected_colours = ['Black','Blue,Over Dye','Bright White', 'Dark Blue Vintage']
    actual_colors = []
    color_options = context.driver.find_elements(*COLOR_OPTIONS)
    for option in color_options:
        option.click()
        actual_colors = context.driver.find_elements(*COLOR_NAME)
        assert actual_colors == expected_colours
    print ("Test Case Passed")



















