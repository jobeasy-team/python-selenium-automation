from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

amzn_choice = (By.CSS_SELECTOR, 'div.a-section.a-spacing-base')
COLOR_OPT = (By.CSS_SELECTOR, '#variation_color_name li[class*="swatch"]')
COLOR_NAME = (By.CSS_SELECTOR, 'div#variation_color_name span.selection')
SEARCH_RES = (By.CSS_SELECTOR, 'span.a-color-state.a-text-bold')


@then("Click on Amazon's Choice")
def select_item(context):
    context.app.search_results_page.select_item()

    '''context.driver.wait.until(EC.element_to_be_clickable(amzn_choice))
    context.driver.find_element(*amzn_choice).click()
    '''

# Lesson 5
@then('Verify user can click through colors')
def ver_color_click(context):
    context.driver.wait.until(EC.element_to_be_clickable(COLOR_OPT))

    exp_colors = ['Black', 'Blue', 'Green', 'White', 'Champagne', 'Rose Gold']
    actual_colors = []

    color_opt = context.driver.find_elements(*COLOR_OPT)
    for option in color_opt:
        option.click()
        color_name = context.driver.find_element(*COLOR_NAME).text
        actual_colors += [color_name]

    assert actual_colors == exp_colors, f'Error, we want {exp_colors} but got{actual_colors}'


@then('Verify search results for {exp_res}')
def ver_search_results(context, exp_res):
    context.app.search_results_page.ver_search_results(exp_res)


    '''act_res = context.driver.find_element(*SEARCH_RES).text
    assert exp_res == act_res, \
    f'Error,{act_res} does not match {exp_res}'''''
