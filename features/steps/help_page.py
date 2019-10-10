from behave import then
from selenium.webdriver.common.by import By


@then('Click go button')
def click_go(context):
    context.driver.find_element(By.XPATH,"//input[@class = 'a-button-input']").click()


@then('Verify cancel items or orders text is present')
def verify_result(context):
    result_text = context.driver.find_element(By.XPATH, "//div[@class='help-content']/h1").text
    assert "Cancel Items or Orders" in result_text, f"Expected cancel orders or items in text, but got {result_text}"