from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome(executable_path='C:\\Users\\vsupe\QA\\Automation\\python-selenium-automation\\chromedriver')
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

# Amazon logo
driver.find_element(By.XPATH, "//i[@aria-label='Amazon']")

# Email field
driver.find_element(By.ID, 'ap_email')

# Continue button
driver.find_element(By.ID, 'continue')

# Need help link
driver.find_element(By.XPATH, "//span[contains(text(),'Need help?')]")

# Forgot your password link
driver.find_element(By.ID, 'auth-fpp-link-bottom')

# Other issues with Sign-In link
driver.find_element(By.ID, 'ap-other-signin-issues-link')

# Create your Amazon account button
driver.find_element(By.ID, 'createAccountSubmit')

# Conditions of use link
driver.find_element(By.XPATH,
                    "//a[@href='/gp/help/customer/display.html/ref=ap_signin_notification_condition_of_use?ie=UTF8"
                    "&nodeId=508088']")

# Privacy Notice link
driver.find_element(By.XPATH,
                    "//a[@href='/gp/help/customer/display.html/ref=ap_signin_notification_privacy_notice?ie=UTF8"
                    "&nodeId=468496']")
