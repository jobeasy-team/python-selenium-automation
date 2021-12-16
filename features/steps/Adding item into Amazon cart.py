from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from behave import given, when, then


searched_item = (By.CSS_SELECTOR, "#twotabsearchtextbox")
selected_item = (By.CSS_SELECTOR, "img[alt='Kurukahveci Mehmet Efendi Turkish Coffee, 17.6 Ounce (Pack of 1)']")

#@given('Open Amazon website (No Sign In)')
#def open_amazon(context):
    #context.driver.get('https://www.amazon.com/ref=nav_logo')
#(Source: "Navigating to Amazon Cart" steps file).


@when('Search for {search_word}')
def search_for(context, search_word):
    context.driver.find_element(*searched_item).send_keys(search_word)
    context.driver.find_element(*searched_item).send_keys(Keys.RETURN)


@when ('Select item')
def select(context):
    context.driver.find_element(*selected_item).click()


@when ('Add item into cart')
def add_into_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-button").click()


#@when('Click on Amazon cart')
#def enter_button(context):
    #context.driver.find_element(By.CSS_SELECTOR, '#nav-cart-text-container').click()
#(Source: "Navigating to Amazon Cart" steps file).

@then('Show {search_word} in cart')
def verify_item_in_cart_text(context, search_word):
    expected_value= context.driver.find_element(By.CSS_SELECTOR,"span.a-truncate.a-size-medium").text
    sleep(5)
    print(expected_value)
    assert search_word == expected_value,f'Item not matching {search_word}'

