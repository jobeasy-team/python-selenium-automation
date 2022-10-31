from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

# Bestseller_links=(By.(By.XPATH, "//*[@id='zg_header']//a")

@given("open Amazon Bestseller page")
def Open_Bestsellers (context):
    context.driver.get("https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers")
    sleep(4)


@then("verify there are five links")
def Bestseller_links(context):
    Bestseller_links= context.driver.find_elements(By.XPATH, "//*[@id='zg_header']//a")
    print(Bestseller_links)
    Links_Number=len(Bestseller_links)
    assert Links_Number==5, f'expexted 5 tabs but got {Links_Number}'





