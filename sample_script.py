from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# init driver
driver = webdriver.Chrome()
driver.maximize_window()
# driver.implicitly_wait(5) # check for element 100ms
driver.wait = WebDriverWait(driver, 5)

# open the url
driver.get('https://www.google.com/')

search = driver.find_element(By.NAME, 'q')
search.clear()
search.send_keys('Dress')


# wait and click search
driver.wait.until(
    EC.element_to_be_clickable((By.NAME, 'btnK213213')),
    message='Search btn was not clickable'
).click()

# wait for 4 sec
# sleep(4)


# verify
assert 'dress' in driver.current_url.lower(), f"Expected query not in {driver.current_url.lower()}"
print('Test Passed')

driver.quit()
