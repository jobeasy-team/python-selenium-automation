from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(executable_path='/Users/Adewale/OneDrive/Desktop/Automation Course/python-selenium-automation/chromedriver')
driver.get('https://www.amazon.com/gp/help/customer/display.html ')


driver.find_element(By.ID, 'helpsearch').send_keys('cancel order')

driver.find_element(By.ID, 'helpsearch').send_keys(Keys.ENTER)

expected_result = 'Cancel Items or Orders'

actual_result = driver.find_element(By.XPATH, "//h1[text()='Cancel Items or Orders']").text

assert expected_result == actual_result, f'Error! Actual text {actual_result} does not match expected {expected_result}'
print ('Test case passed')

driver.quit()