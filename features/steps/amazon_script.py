from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome(executable_path='/Users/bkarp0518/Desktop/Automation/python-selenium-automation/chromedriver')
driver.maximize_window()
driver.implicitly_wait(5)

driver.get('https://www.amazon.com/')

driver.find_element(By.ID, 'twotabsearchtextbox') .send_keys('Table')

search_icon = driver.find_element(By.ID, 'nav-search-submit-button').click()

actual_result = driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
print(f'Actual result: {actual_result}')
expected_result = '"Table"'

assert expected_result == actual_result, f'Expected {expected_result}, but got {actual_result}'

driver.quit()
