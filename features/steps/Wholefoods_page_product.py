from selenium.webdriver.common.by import By
from behave import given, when, then

@given('Open Wholefoods page')
def open_wholefoods(context):
    context.driver.get('https://www.amazon.com/wholefoodsdeals')

@then('Verify if regular appears on every product')
def verify_product(context):
    expected_product = ['Regular $14.99/lb', 'Regular $29.99/lb', 'Regular $2.99 - $54.99 ea', 'Regular prices vary', 'Regular $2.99-$14.99 ea']
    regular_text = context.driver.find_elements(By. CSS_SELECTOR, "span.a-size-large.wfm-sales-item-card__prime-price.a-text-bol")


    for i in range(len(regular_text)):
       regular_text[i].click()
       actual_text = context.driver.find_element(By.CSS_SELECTOR, "div.s-item-container").text
       assert actual_text == expected_product[i], f'Error, product is {actual_text}, but expected {expected_product[i]}'

