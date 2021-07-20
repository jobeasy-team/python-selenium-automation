from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open Amazon page')
def open_amazon(context):
    #context.driver.get('https://www.amazon.com/')
    context.app.main_page.open_main()


@when('Input Table in search field')
def search_amazon(context):
    #context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('Table', Keys.RETURN)
    context.app.header.input_search('Table')


@when('Click On Amazon search icon')
def click_search(context):
    #context.driver.find_element(By.ID, 'nav-search-submit-button').click()
    context.app.header.click_search()


@then('Verify search worked')
def verify_search_worked(context):
    #actual_result = context.driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
    #expected_result = '"Table"'
    #assert expected_result == actual_result, f'Expected {expected_result}, but got {actual_result}'
    context.app.search_results_page.verify_search_worked()


@then('Verify HPC department is selected')
def verify_hpc_department(context):
    pass