from selenium.webdriver.common.by import By
from behave import given, when, then


@given('open Amazon web page')
def open_web_page (context):
    context.driver.get('https://www.amazon.com/')


@when('user insert for shoes')
def insert_shoe_to_search(context):
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys("shoes")
    context.driver.find_element(By.ID, 'nav-search-submit-button').click()



