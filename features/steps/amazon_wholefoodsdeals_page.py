from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait
from behave import given, when, then
from time import sleep

PRODUCT_DESCRIPTION = (By.XPATH, "//div[@id = 'wfm-pmd_deals_section']//span[contains(@class, "
                                 "'wfm-sales-item-card__prime-price') and contains (text(), 'PRIME')]/ancestor::div["
                                 "contains(@class, 'a-text-left')]")


@given('User opens Amazon wholefoodsdeals page and maximizes window')
def open_amazonwholefoodsdeals(context):
    context.driver.get('https://www.amazon.com/wholefoodsdeals')
    context.driver.maximize_window()
    sleep(4)


@then('Verifies every product listed with Prime benefit has product name and Regular price')
def verify_regular_price_in_prime_section_menu(context):
    prime_sale_items = context.driver.find_elements(*PRODUCT_DESCRIPTION)
    print(len(prime_sale_items))

    for regular_price in prime_sale_items:
        assert 'Regular' in regular_price.text

    '''if 'Regular' in regular_price.text:
            print('NEW\n'+regular_price.text)'''




