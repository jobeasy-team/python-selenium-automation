from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


@given('open amazon page')
def open_amazon(context):
    context.driver.get("https://www.amazon.com/")
    sleep(1)



@when('search for customer service')
def open_customer_service(context):
    context.driver.get("https://www.amazon.com/gp/help/customer/display.html")
    sleep(1)



@then('search for canceled items')
def open_canceled_items(context):
    context.driver.find_element(By.XPATH, "//input[@type='search']").send_keys('cancel order', Keys.ENTER)
    sleep(2)




@then('verify the canceled item or order page comes')
def verify_canceled_page(context):
    expected_result = 'Cancel Items or Orders You can cancel items or orders that have not shipped by visiting the Order ' \
                      'section in Your Account '
    actual_result = context.driver.find_element(By.XPATH, "//div[@class='a-box a-spacing-extra-large answer-box answer-box-t1']").text

    assert expected_result == actual_result, f'Error! Actual text {actual_result} does not match expected{expected_result}'








