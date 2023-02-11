from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.service import Service

# driver = webdriver.Chrome(executable_path='/Users/svetlanalevinsohn/JobEasy/13-python-selenium-automation/chromedriver')
service = Service('/Users/svetlanalevinsohn/JobEasy/13-python-selenium-automation/chromedriver')
driver = webdriver.Chrome(service=service)

driver.get('https://www.amazon.com/')

driver.find_element(By.XPATH, "//span[contains(text(), '& Orders')]").click()
driver.find_element(By.XPATH, "//h1[contains(text(), 'Sign in')]").is_displayed()

# Not sure what I'm doing wrong but I'm not sure I understand what to put in expected_result or how to handle needing
# to check multiple things
# expected_result1 = '"Sign in is Displayed"'
# actual_result1 = driver.find_element(By.XPATH, "//h1[contains(text(), 'Sign in')]").is_displayed()
expected_result2 = 'input'
actual_result2 = driver.find_element(By.ID,  'ap_email')

print(actual_result2)

# assert expected_result1 == actual_result1, f'Expected {expected_result1} but got actual {actual_result1}'
assert expected_result2 == actual_result2, f'Expected {expected_result2} but got actual {actual_result2}'
print('Test case passed')

driver.quit()
