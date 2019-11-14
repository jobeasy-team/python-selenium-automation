from selenium.webdriver.common.by import By
from behave import when, then
from time import sleep

TOOLBAR_TEXT_BOLD = (By.CSS_SELECTOR, "h1 span.a-text-bold")
PRODUCT_RESULT = (By.XPATH,
                  "//span[@class='celwidget slot=SEARCH_RESULTS template=SEARCH_RESULTS widgetId=search-results "
                  "index=0']//img[@class='s-image']")


@when('Open the first product search result')
def click_first_result(context):
    context.driver.find_element(*PRODUCT_RESULT).click()
    sleep(1.5)


@then('Search result for {product} is shown')
def verify_result(context, product):
    # result_text = context.driver.find_element(*TOOLBAR_TEXT_BOLD).text
    # # assert result_text == '"dress"', f"Expected text is dress but got {result_text}"
    # assert product in result_text, f"Expected text is dress but got {result_text}"
    context.app.search_results.verify_result_shown(product)
