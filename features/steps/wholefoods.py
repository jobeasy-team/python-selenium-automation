from selenium.webdriver.common.by import By
from behave import given, when, then

WHOLEFOODS_ITEMS = (By.XPATH, "//li[@class='s-result-item' and .//span[contains(@class, prime-price)]]")
PRODUCT_NAME = (By.CSS_SELECTOR, "span.wfm-sales-item-card__product-name")

@given('Open Amazon Wholefoods page')
def open_wholefoods(context):
    context.driver.get('https://www.amazon.com/wholefoodsdeals')


@then('Verify that Wholefoods products have regular prices and names')
def verify_wholefoods_items(context):
    wholefoods_items = context.driver.find_elements(*WHOLEFOODS_ITEMS)
    for i in wholefoods_items:
        assert 'Regular' in i.text, f'Expected Regular price not found in {i.text}'
        product_name = i.find_element(*PRODUCT_NAME).text
        print(product_name)
        assert product_name, f'Product name is missing'


