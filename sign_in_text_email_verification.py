from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.service import Service

# driver = webdriver.Chrome(executable_path='/Users/svetlanalevinsohn/JobEasy/13-python-selenium-automation/chromedriver')
service = Service('/Users/svetlanalevinsohn/JobEasy/13-python-selenium-automation/chromedriver')
driver = webdriver.Chrome(service=service)

# Test Case: Logged out user sees Sign in page when clicking Orders
driver.get('https://www.amazon.com/')
sleep(2)
driver.find_element(By.ID, 'nav-orders').click()

expected_result = 'Sign in'
actual_result = driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text

assert expected_result == actual_result, f'Expected {expected_result} but found {actual_result}'

#Verify email field present
#you can just ask driver to find element if it's not found it will return no element exeption '
# OR

assert driver.find_element(By.ID, 'ap_email').is_displayed(), 'Email field not shown'
driver.quit()
