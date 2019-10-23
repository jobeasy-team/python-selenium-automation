from selenium.webdriver.common.by import By
from time import sleep
from behave import given, then

BENEFIT_BOXES = (By.XPATH, "//div[contains(@class, 'a-section benefit-box')]")


@given('User opens Amazon Prime page')
def open_amazonprime(context):
    context.driver.get('https://www.amazon.com/amazonprime')
    context.driver.maximize_window()
    sleep(2)


@then('Verifies {expected_box_count} benefit boxes are present')
def verify_box_count(context, expected_box_count):
    actual_box_count = len(context.driver.find_elements(*BENEFIT_BOXES))
    print(f"Number of benefit boxes equals to {actual_box_count}")
    assert actual_box_count == int(expected_box_count), \
        print(f"Expected {expected_box_count} benefit boxes,"
              f"but got{actual_box_count}")
