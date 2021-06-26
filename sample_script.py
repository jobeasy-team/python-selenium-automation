from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# init driver
driver = webdriver.Chrome(executable_path='/Users/bkarp0518/Desktop/Automation/python-selenium-automation/chromedriver')
driver.maximize_window()

# Implicit wait
# Checks 100 ms for webelement (0.1 sec)
# Only works with find_element
driver.implicitly_wait(4)

# open the url
driver.get('https://www.google.com/')

search = driver.find_element(By.NAME, 'q')
search.clear()
search.send_keys('Dress')

# wait for 4 sec
#sleep(4)

# Explicit wait
# Checks every 500 ms for condition (0.5 sec)
driver.wait = WebDriverWait(driver, 15)
e = driver.find_element(By.NAME, 'btnK').click()

# click search


# verify
assert 'dress' in driver.current_url.lower(), f"Expected query not in {driver.current_url.lower()}"
print('Test Passed')

driver.quit()
