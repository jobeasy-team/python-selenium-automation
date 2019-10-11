from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome()

# open the url
driver.get('https://www.amazon.com')
driver.maximize_window()

sleep(1)

# Customer Service (Help) link
driver.find_element(By.LINK_TEXT, 'Customer Service').click()

sleep(1)

search = driver.find_element(By.ID, 'helpsearch')
search.clear()
search.send_keys('cancel order')

sleep(1)

# click search
driver.find_element(By.ID, 'helpSearchSubmit').click()

sleep(1)

# verify
assert 'Cancel Items or Orders' in driver.page_source

sleep(2)

driver.quit()
