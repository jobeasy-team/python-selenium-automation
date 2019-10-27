from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait
from behave import given, when, then
from time import sleep

PRODUCT_DESCRIPTION = (By.XPATH, "//div[@id = 'wfm-pmd_deals_section']//span[contains(@class, "
                                 "'wfm-sales-item-card__prime-price') and contains (text(), 'PRIME')]/ancestor::div["
                                 "contains(@class, 'a-text-left')]")
PRODUCT_NAME = (By.XPATH,
                "//div[@id = 'wfm-pmd_deals_section']//span[contains(@class, 'wfm-sales-item-card__prime-price') and contains (text(), 'PRIME')]//ancestor::div[contains(@class, 'a-text-left')]//child::span[contains(@class, 'wfm-sales-item-card__product-name')]")


@given('User opens Amazon wholefoodsdeals page and maximizes window')
def open_amazonwholefoodsdeals(context):
    context.driver.get('https://www.amazon.com/wholefoodsdeals')
    context.driver.maximize_window()
    sleep(4)


@then('Verifies every product listed with Prime benefit has Regular price and Name')
def verify_regular_price_in_prime_section_menu(context):
    prime_sale_items = context.driver.find_elements(*PRODUCT_DESCRIPTION)
    print(len(prime_sale_items))
    names_of_products = context.driver.find_elements(*PRODUCT_NAME)

    for regular_price in prime_sale_items:
        assert 'Regular' in regular_price.text

        if 'Regular' in regular_price.text:
            #print('NEW\n'+regular_price.text)
            print(prime_sale_items.index(regular_price))
        else:
            print(prime_sale_items.index(regular_price), regular_price.text)

    for name in names_of_products:
        print(name.text)
        """for product_description in names_of_products:
                assert name.text in product_description.text"""


    '''for name in name_of_a_product
        assert name.text in regular_price.text'''



