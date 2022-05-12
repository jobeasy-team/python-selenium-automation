from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys
from time import sleep

@given('open amazon best seller page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')


@when('Verify links are present')
def customer_search(context):
    context.driver.find_element(By.XPATH,"//a[@href='/Best-Sellers/zgbs/ref=zg_bs_tab']")
    expected_result = 'Best Sellers'
    actual_result = context.driver.find_element(By.XPATH, "//a[@href='/Best-Sellers/zgbs/ref=zg_bs_tab']").text
    context.driver.find_element(By.XPATH, "//a[@href='/Best-Sellers/zgbs/ref=zg_bs_tab']")
    expected_result = 'New Releases'
    actual_result = context.driver.find_element(By.XPATH, "//a[@href='/Best-Sellers/zgbs/ref=zg_bs_tab']").text
    context.driver.find_element(By.XPATH, "//a[@href='/gp/movers-and-shakers/ref=zg_bs_tab']")
    expected_result = 'Movers & Shakers'
    actual_result = context.driver.find_element(By.XPATH, "//a[@href='/gp/movers-and-shakers/ref=zg_bs_tab']").text
    context.driver.find_element(By.XPATH, "//a[@href='/gp/most-wished-for/ref=zg_bs_tab']")
    expected_result = 'Most Wished For'
    actual_result = context.driver.find_element(By.XPATH, "//a[@href='/gp/most-wished-for/ref=zg_bs_tab']").text
    context.driver.find_element(By.XPATH, "//a[@href='/gp/most-gifted/ref=zg_bs_tab']")
    expected_result = 'Gift Ideas'
    actual_result = context.driver.find_element(By.XPATH, "//a[@href='/gp/most-gifted/ref=zg_bs_tab']").text
    print ("Test Case Passed")
















