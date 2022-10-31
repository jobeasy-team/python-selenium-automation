from selenium.webdriver.common.by import By
from behave import when, then
from time import sleep

ITEM=(By.XPATH, "//div[@cel_widget_id='MAIN-SEARCH_RESULTS-3']")

@when('select Item')
def select_item(context):
    context.driver.find_element(*ITEM).click()
