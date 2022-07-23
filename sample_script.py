from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# init driver
driver = webdriver.Chrome(executable_path='/Users/svetlanalevinsohn/JobEasy/11-python-selenium-automation/chromedriver')
driver.maximize_window()

# driver.implicitly_wait(5)  # 100 ms

driver.wait = WebDriverWait(driver, 10)

# open the url
driver.get('https://www.google.com/')

search = driver.find_element(By.NAME, 'q')
search.clear()
search.send_keys('coffee')

# wait for 4 sec
# sleep(4)
search_btn = (By.NAME, 'btnK')
driver.wait.until(EC.element_to_be_clickable(search_btn), message='Search btn not clickable').click()

# verify
assert 'coffee' in driver.current_url.lower(), f"Expected query not in {driver.current_url.lower()}"
print('Test Passed')

driver.quit()
