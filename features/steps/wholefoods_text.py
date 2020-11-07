from behave import given, then
from selenium.webdriver.common.by import By

PRODUCT_NAME = (By.CSS_SELECTOR, '.wfm-sales-item-card__product-name')


@given('Open amazon wholefoods page')
def open_wholefoods_page(context):
    context.driver.get('https://www.amazon.com/wholefoodsdeals')


@then('Verify the text Regular')
def look_text(context):
    text = context.driver.find_elements(By.ID, 'wfm-pmd_deals_section')
    for i in text:
        assert "Regular" in i.text, f"Expected 'Regular' to be in {i.text}"
        assert i.find_element(*PRODUCT_NAME)
