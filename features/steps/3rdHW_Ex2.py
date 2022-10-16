from selenium.webdriver.common.by import By
from behave import given, when, then

@given('user opens the website')
def open_amazon_website(context):
    context.driver.get('https://www.amazon.com/')


    @when ('user click on Orders')
    def Click_on_order (context):
        context.driver.find_element(By.XPATH, "//span[@class ='nav-line-1']").click()


