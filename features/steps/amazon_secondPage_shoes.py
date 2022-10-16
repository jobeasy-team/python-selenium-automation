from selenium.webdriver.common.by import By
from behave import given, when, then

@then ('result for shoes are shown')
def verify_found_results_text(context):
    expected_result= "shoes"
    actual_result= context.driver.find_element(By.XPATH, "//div[@class='a-section a-spacing-small a-spacing-top-small']//span[@class='a-color-state a-text-bold']")
    assert expected_result== actual_result,  f"Error|Expected {expected_result}, but got, {actual_result}"
