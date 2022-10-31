from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_BOX=(By.ID, "twotabsearchtextbox")
SEARCH_BTN=(By.ID, "nav-search-submit-button")

@when('search for item')
def search_for_item(context):
    context.driver.find_element(*SEARCH_BOX).send_keys('okley flak')
    context.driver.find_element(*SEARCH_BTN).click()

