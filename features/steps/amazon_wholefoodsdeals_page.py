from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait
from behave import given, when, then
from time import sleep

PRODUCT_DESCRIPTION = (By.XPATH, "//div[@id = 'wfm-pmd_deals_section']//span[contains(@class, "
                                 "'wfm-sales-item-card__prime-price') and contains (text(), 'PRIME')]/ancestor::div["
                                 "contains(@class, 'a-text-left')]")
PRODUCT_NAME = (By.XPATH, "//div[@id = 'wfm-pmd_deals_section']//span[contains(@class, 'wfm-sales-item-card__prime-price') and contains (text(), 'PRIME')]//ancestor::div[contains(@class, 'a-text-left')]//child::span[contains(@class, 'wfm-sales-item-card__product-name')]")


@given('User opens Amazon wholefoodsdeals page and maximizes window')
def open_amazonwholefoodsdeals(context):
    context.driver.get('https://www.amazon.com/wholefoodsdeals')
    context.driver.maximize_window()
    sleep(4)


@then('Verifies every product listed with Prime benefit has Regular price and Name')
def verify_regular_price_in_prime_section_menu(context):
    prime_sale_items = context.driver.find_elements(*PRODUCT_DESCRIPTION)
    context.driver.find_elements(*PRODUCT_NAME)
    print(len(prime_sale_items))

    for regular_price in prime_sale_items:
        assert 'Regular' in regular_price.text

        product_name = regular_price.find_element(*PRODUCT_NAME).text
        assert '' != product_name, f"Expected non-empty product name"

        if 'Regular' in regular_price.text:
            print(prime_sale_items.index(regular_price))
        else:
            print(prime_sale_items.index(regular_price), regular_price.text)




