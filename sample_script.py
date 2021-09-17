from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome(executable_path='/Users/svetlanalevinsohn/JobEasy/7-python-selenium-automation/chromedriver')
driver.maximize_window()

driver.get('https://www.google.com/')

search_field = driver.find_element(By.NAME, 'q')
search_field.send_keys('Dress')

sleep(4)
driver.find_element(By.NAME, 'btnK').click()

assert 'Dress' in driver.current_url, f'Error! the URL does not have the word Dress'

print('Test case passed')

driver.quit()