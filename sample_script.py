from time import sleep
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome(r'C:\Users\ababa\Desktop\QA Automation\PythonSeleniumAutomation\python-selenium-automation\chromedriver.exe')
driver.maximize_window()
# driver.implicitly_wait(4)  # 100 ms
driver.wait = WebDriverWait(driver, 10)  # 500 ms

# open the url
driver.get('https://www.google.com/')

search = driver.find_element(By.NAME, 'q')
search.clear()
search.send_keys('Dress')

# wait for 4 sec
# sleep(4)

# click search
# driver.find_element(By.NAME, 'btnK').click() ***THIS IS PREVIOUS STEP. NEW STEP BELOW:
element = driver.wait.until(EC.element_to_be_clickable((By.NAME, 'btnK')), message='Search button not found')
element.click()
# verify
assert 'dress' in driver.current_url.lower(), f"Expected query not in {driver.current_url.lower()}"
print('Test Passed')

driver.quit()
