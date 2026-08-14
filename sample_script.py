from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# init driver
driver = webdriver.Chrome()
driver.maximize_window()
# driver.implicitly_wait(4) # set it once => check for element to be present every 100 ms (1/10 sec)

driver.wait = WebDriverWait(driver, timeout=10)  # set it where it's used => check for condition to be met every 1/2s

# open the urlproduct_in_cart
driver.get('https://www.google.com/')

search = driver.find_element(By.NAME, 'q')
search.clear()
search.send_keys('Dress')

# wait for 4 sec
# sleep(4)

# click search
search_btn = (By.NAME, 'btnK')
driver.wait.until(EC.element_to_be_clickable(search_btn), message=f'Button not clickable by {search_btn}').click()
# driver.find_element(*search_btn).click()

# verify
assert 'dress' in driver.current_url.lower(), f"Expected query not in {driver.current_url.lower()}"
print('Test Passed')

driver.quit()
