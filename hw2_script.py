from time import sleep
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome()
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/gp/help/customer/display.html')

search = driver.find_element(By.ID, 'helpsearch')
search.clear()
search.send_keys('cancel order')
search.send_keys(Keys.RETURN)

# assertion
result = driver.find_element(By.XPATH, "//b[contains(text(),'cancel order')]").text
expected_result = 'cancel order'
assert expected_result == result, f'error, actual {result} did not match {expected_result}'
print('Test Passed')

driver.quit()

