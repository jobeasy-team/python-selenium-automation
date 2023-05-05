from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.service import Service

# driver = webdriver.Chrome(executable_path='/Users/svetlanalevinsohn/JobEasy/13-python-selenium-automation/chromedriver')
service = Service('/Users/svetlanalevinsohn/JobEasy/13-python-selenium-automation/chromedriver')
driver = webdriver.Chrome(service=service)

# by ID
driver.find_element(By.ID, 'twotabsearchtextbox')

# By CSS, using ID Syntax tag#ID but you can omit tag. instead of  'input#twotabsearchtextbox'use '#twotabsearchtextbox'
driver.find_element(By.CSS_SELECTOR, '#twotabsearchtextbox')
