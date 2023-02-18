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
expected_text = 'Sign in'
actual_text = driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
expected = 'input'
assert driver.find_element(By.ID, 'ap_email').is_displayed(), 'Email field not shown'

assert actual_text == expected_text, f'Expected {expected_text} but got {actual_text}'
print('Test case passed')

driver.quit()

