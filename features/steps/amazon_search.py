from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open Amazon page')
def open_amazon(context):
    context.app.main_page.open_main()


@when('Click on Amazon search icon')
def click_search(context):
    #context.driver.find_element(By.ID, 'nav-search-submit-button').click()
    context.app.header.click_search()

@when('Search for {search_word}')
def search_for_product(context, search_word):
    #context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys(search_word, Keys.ENTER)
    context.app.header.input_search()

@when('Click on the first product')
def click_first_product(context):
    context.driver.find_element(By.XPATH, '//*[@data-component-id="1"]').click()


@when('Click on Add to Cart button')
def click_add_to_cart_btn(context):
    # if len(context.driver.find_elements(By.ID, 'native_dropdown_selected_size_name')) == 1:
    #     context.driver.find_element(By.ID, 'native_dropdown_selected_size_name').click()
    #     context.driver.find_element(By.ID, 'size_name_2').click()
    #     sleep(3)
    context.driver.find_element(By.ID, 'add-to-cart-button').click()


@then('Verify search worked')
def verify_search_worked(context):
    # actual_result = context.driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
    # expected_result = '"Table"'
    # assert expected_result == actual_result, f'Expected {expected_result}, but got {actual_result}'
    context.app.search_results.verify_search_worked()

@then('Verify user can select colors')
def click_through_colors(context):
    colors = context.driver.find_elements(By.CSS_SELECTOR, 'img.imgSwatch')
    count = 0
    for color in colors:
        context.driver.find_element(By.CSS_SELECTOR, 'img.imgSwatch').click()
        count += 1
    assert len(colors) == count, f'Expected {len(colors)}, but got {count}'
