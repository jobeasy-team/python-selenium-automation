from selenium.webdriver.common.by import By
from behave import given, when, then

PRODUCT_COUNT = (By.CSS_SELECTOR, 'div.s-result-item')

@then('Verify product has name and image')
def verify_product_name_and_image(context):
    number_of_products = context.driver.find_elements(*PRODUCT_COUNT)
    print(number_of_products)

    item = 1
    for product in number_of_products[:5]:
        item += 1
        link = '[data-component-type="s-search-result"][data-index= \"' + str(item) + '\"] span.a-size-base-plus'
        PRODUCT_NAME = (By.CSS_SELECTOR, link)
        name = context.driver.find_element(*PRODUCT_NAME).text
        print(name)

        image_link = '[data-component-type="s-search-result"][data-index= \"' + str(item) + '\"] img.s-image'
        product_image = context.driver.find_element(By.CSS_SELECTOR, image_link).is_displayed

        assert product_image and name != "", f'Product name {name} and Image {product_image} is not displayed'
