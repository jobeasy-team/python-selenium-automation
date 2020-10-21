from behave import given, when, then
from selenium.webdriver.common.by import By
#from selenium import webdriver
from selenium.webdriver.common.keys import Keys

SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
SEARCH_ICON = (By.XPATH,"//input[@value='Go']")

@given('Open Amazon home page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')

@when('Search for kettle')
def input_search_word(context):
    search1 = context.driver.find_element(*SEARCH_INPUT).send_keys('kettle')

@Then('Click on the search icon')
def click_search_icon(context):
    search_icon = context.driver.find_element(*SEARCH_ICON)
    search_icon.click()

@Then('Select first product to cart')
def first_product(context):
    first_product = context.driver.find_element(By.XPATH, "//img[@src='https://m.media-amazon.com/images/I/812C5q3i5+L._AC_UL320_.jpg']")
    first_product.click()

@Then('Add product in cart')
def add_cart(context):
    add_cart = context.driver.find_element(By.ID, "//input[@id = 'add-to-cart-button']")
    add_cart.click()

@Then('Verify the product in cart')
def verify_cart(context):
    verify_cart = context.driver.find_element(By.XPATH, ("//span[@id='nav-cart-count']")





