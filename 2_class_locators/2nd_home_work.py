from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(
    executable_path="C:/ProgramData/Microsoft/Windows/Start Menu/Programs/JetBrains/chromedriver.exe")
driver.get("https://www.amazon.com/gp/help/customer/display.html")

ama = driver.find_element(By.XPATH, "//input[@type='search']")

ama.send_keys('cancel order', Keys.ENTER)

expected_result = 'Cancel Items or Orders You can cancel items or orders that have not shipped by visiting the Order ' \
                  'section in Your Account '

actual_result = driver.find_element(By.XPATH, "//div[@class='a-box a-spacing-extra-large answer-box answer-box-t1']").text

assert expected_result == actual_result, f'Error! Actual text {actual_result} does not match expected{expected_result}'

print('Test case passed')
