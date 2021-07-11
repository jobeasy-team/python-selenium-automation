from selenium.webdriver.common.by import By
from behave import given, when, then

BEST_DEALS_ITEMS = (By.XPATH, "//li[@class='s-result-item' and .//span[contains(@class,'prime-price')]]/div")
PRODUCT_NAME = (By.CSS_SELECTOR, "span.wfm-sales-item-card__product-name")

@given('Open Wholefoods page')
def open_wholefoods(context):
    context.driver.get('https://www.amazon.com/wholefoodsdeals')



@then('Verify that Wholefoods products have regular prices and names')
def verify_best_deals(context):
    # Let's find all the products and store them into best_deals_items
    best_deals_items= context.driver.find_elements(*BEST_DEALS_ITEMS)
    # Now, let's loop through all of them
    for e in best_deals_items:
        # and verify that every element has a test Regular in it
        assert 'Regular' in e.text, f'Expected Regular price not found in {e.text}'
        # and a product name
        product_name = e.find_element(*PRODUCT_NAME).text
        print(product_name)
        assert product_name, f'Product name is missing'