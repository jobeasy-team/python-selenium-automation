from selenium.webdriver.common.by import By
from behave import then

TOOLBAR_TEXT_BOLD = (By.CSS_SELECTOR, "h1 span.a-text-bold")

@then('Search results for {product} is shown')
def verify_result(context, product):
    result_text = context.driver.find_element(*TOOLBAR_TEXT_BOLD).text
    #assert result_text == '"dress"', f"Expected text is dress but got {result_text}"
    assert product in result_text, f"Expected text is dress but got {result_text}"