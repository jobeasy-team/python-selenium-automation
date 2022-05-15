from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

cstmr_svc_bar = (By.ID, 'hubHelpSearchInput')
search = (By.ID, 'twotabsearchtextbox')


@given('Open Amazon Customer Service Page')
def open_cstmr_svc_page(context):
    context.driver.get("https://www.amazon.com/gp/help/customer/display.html")
    sleep(5)


@when('Search for {keyword}')
def cstmr_svc_search(context, keyword):
    context.driver.find_element(*search).send_keys(keyword)
    context.driver.find_element(*search).send_keys(Keys.RETURN)
    sleep(5)
