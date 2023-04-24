from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(executable_path='/Users/ekaterinasuvorova/Automation2023/python-selenium-automation/chromedriver')

# By ID
driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('table')

# By XPath,tag and attribute
driver.find_element(By.XPATH, "//input[@placeholder='Search Amazon']")
driver.find_element(By.XPATH, "//input[@aria-label='Search Amazon']")

# By xpath, multiple attributes
driver.find_element(By.XPATH, "//a[@aria-label='Amazon'and @href='/ref=nav_logo' ]")