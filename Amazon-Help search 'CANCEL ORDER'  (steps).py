from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver= webdriver.Chrome(executable_path='/Users/ababa/Desktop/QA Automation/PythonSeleniumAutomation/python-selenium-automation/chromedriver.exe')
driver.get('https://www.amazon.com/gp/help/customer/display.html')

driver.find_element(By.ID, 'helpsearch').send_keys('cancel order')
driver.find_element(By.ID, 'helpsearch').send_keys(Keys.RETURN)

#Verify that ‘Cancel Items or Orders’ text is present
actual_result = driver.find_element(By.XPATH, "//div/h1").text
expected_result = "Cancel Items or Orders"

assert actual_result == expected_result, f"ERROR, actual {actual_result} did not match {expected_result}"

print('TEST CASE PASSED.')
driver.quit()


