from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# driver = webdriver.Chrome(executable_path='/Users/svetlanalevinsohn/JobEasy/13-python-selenium-automation/chromedriver')


#css selector for amazon icon/logo
diver.find_element(By.CSS_SELECTOR, 'i.a-icon-logo')

#css selector for create account lable
diver.find_element(By.CSS_SELECTOR, 'h1')

#css selector for name input field
diver.find_element(By.CSS_SELECTOR, 'input#ap_customer_name')

#css selector for Email input field
diver.find_element(By.CSS_SELECTOR, 'input#ap_email')

#css selector for Retype Password input field
diver.find_element(By.CSS_SELECTOR, 'input#ap_password_check')

#css selector for Continue button
diver.find_element(By.CSS_SELECTOR, 'input#continue')

#css selector for condition of use
diver.find_element(By.CSS_SELECTOR, 'div#legalTextRow a[href*="condition_of_use?"]')

#css selector for privacy notice
diver.find_element(By.CSS_SELECTOR, 'div#legalTextRow a[href*="privacy_notice"]')

#css selector for Sign in
diver.find_element(By.CSS_SELECTOR, 'div.a-row a[href*="signin"]')
