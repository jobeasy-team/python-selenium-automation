from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='/Users/jemitpatel/Automation/python-selenium-automation/chromedriver')
driver.get('https://www.amazon.com/')

driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('coffee')
driver.find_element(By.ID, 'nav-search-submit-button').click()