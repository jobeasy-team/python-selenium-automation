

from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

F_ITEM = (By.XPATH, "//span[@class='a-price-whole']")
CART = (By.ID, 'add-to-cart-button')
BB_SEARCH = (By.ID, 'twotabsearchtextbox')
#B_SEL = (By.CSS_SELECTOR, "div._p13n-zg-nav-tab-all_style_zg-tabs-li-selected-div__3tHnP a")


@when('input {search_word}')
def input_word(context, search_word):
    context.driver.find_element(*BB_SEARCH).send_keys('basketball', Keys.ENTER)
    sleep(1)


@then('click on the {search_word}')
def click_on_first_price(context, search_word):
    context.driver.find_element(*F_ITEM).click()
    sleep(1)

@then('click to {search_word}')
def click_on_add(context, search_word):
    context.driver.find_element(*CART).click()
    sleep(1)
#    context.driver.find_element(*B_SEL).click()
#    sleep(1)