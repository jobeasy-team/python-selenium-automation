from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='/Users/jemitpatel/Automation/python-selenium-automation/chromedriver')
driver.get('https://www.amazon.com/')

driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('coffee')

driver.find_element(By.ID, 'nav-search-submit-button').click()

expected_result = '"coffee"'
actual_result = driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text

assert expected_result == actual_result, f'Error! Actual text {actual_result} does not match expected {expected_result}'

print('Test case passed')

driver.quit()