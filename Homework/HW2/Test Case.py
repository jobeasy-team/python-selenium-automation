from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.service import Service

# driver = webdriver.Chrome(executable_path='/Users/svetlanalevinsohn/JobEasy/13-python-selenium-automation/chromedriver')
service = Service('C:\chromedriver.exe')
driver = webdriver.Chrome(service=service)

# open amazon
driver.get('https://www.amazon.com/')

# click orders
driver.find_element(By.XPATH, "//span[@class='nav-line-2' and contains(text(),'& Orders')]").click()

#phase 1
expected_result = 'Sign in'
actual_result = driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
print(actual_result)

assert expected_result == actual_result, f'Expected {expected_result} but got actual {actual_result}'
print('Test case passed')

#phase 2
expected_result = driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']")
actual_result = driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']")
print(actual_result)

assert expected_result == actual_result, f'Expected {expected_result} but got actual {actual_result}'
print('Test case passed')
driver.quit()
