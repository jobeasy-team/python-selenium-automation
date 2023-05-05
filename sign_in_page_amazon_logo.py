from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.service import Service

# driver = webdriver.Chrome(executable_path='/Users/svetlanalevinsohn/JobEasy/13-python-selenium-automation/chromedriver')
service = Service('/Users/svetlanalevinsohn/JobEasy/13-python-selenium-automation/chromedriver')
driver = webdriver.Chrome(service=service)

# Test 'Verify Amazon logo is present on Sign In page'
driver.get('https://www.amazon.com/')
sleep(3)
driver.find_element(By.ID, 'nav-link-accountList').click()

#expected_result = True
#actual_result = driver.find_element(By.XPATH, "//i[@aria-label='Amazon']").is_displayed()
#assert actual_result == expected_result, 'Amazon logo not shown'

assert driver.find_element(By.XPATH, "//i[@aria-label='Amazon']").is_displayed(), 'Amazon logo not shown'

driver.quit()



