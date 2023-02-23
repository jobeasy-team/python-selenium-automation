from selenium.webdriver.common.by import By
from behave import given, when, then

CUSTOMER_SERVICE = (By.CSS_SELECTOR, 'a[href*="ref_=nav_cs_customerservice"]')
WELCOME_TITLE = (By.CSS_SELECTOR, 'h1.fs-heading.bolded')
LIST_OF_SERVICES = (By.CSS_SELECTOR, 'div.issue-card-container')
HELP_TITLE = (By.CSS_SELECTOR, 'label h2.fs-heading.bolded')
SEARCH_FIELD = (By.ID, 'hubHelpSearchInput')
HELP_TOPICS_TITLE = (By.XPATH, '//h2[text()="All help topics"]')
HELP_TOPICS = (By.CSS_SELECTOR, 'ul.help-topics')


@when('Click on Customer service tab')
def click_customer_service_tab(context):
    context.driver.find_element(*CUSTOMER_SERVICE).click()


@then('Verify Welcome title is present')
def verify_welcome_title(context):
    assert context.driver.find_element(*WELCOME_TITLE).is_displayed(), f'Welcome title is mot present'


@then('Verify list of services are present')
def verify_list_of_services(context):
    assert context.driver.find_element(*HELP_TITLE).is_displayed(), 'Help title is not present'


@then('Verify Help title is present')
def verify_list_of_services(context):
    assert context.driver.find_element(*LIST_OF_SERVICES).is_displayed(), 'List of services are not present'


@then('Verify search field is present')
def verify_list_of_services(context):
    assert context.driver.find_element(*SEARCH_FIELD).is_displayed(), 'Search field is not present'


@then('"All help topics" title is present')
def verify_list_of_services(context):
    assert context.driver.find_element(*HELP_TOPICS_TITLE).is_displayed(), 'Help topics title is not present'


@then('List of all help topics is present')
def verify_list_of_services(context):
    assert context.driver.find_element(*HELP_TOPICS).is_displayed(), 'List of all help topics is not present'
