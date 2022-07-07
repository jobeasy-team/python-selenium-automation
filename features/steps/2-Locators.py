from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(r'C:\Users\ababa\Desktop\QA Automation\PythonSeleniumAutomation\python-selenium-automation\chromedriver.exe')


#AMAZON LOCATORS
#1.Amazon logo
driver.find_element(By.XPATH,"//i[contains(@class,'a-icon a-icon-logo')]")


#2.Email field
driver.find_element(By.XPATH, "//input[@type='email']")
driver.find_element(By.XPATH, "//input[@id='ap_email']")


#3.Continue button
driver.find_element(By.XPATH, "//input[@id='continue' and @tabindex='5']")
driver.find_element(By.XPATH, "//input[@tabindex='5' and @class='a-button-input']")


#4.Need help link
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")


#5.Forgot your password link
driver.find_element(By.XPATH, "//a[contains(@href, 'forgotpassword')]")


#6.Other issues with Sign-In link
driver.find_element(By.XPATH, "//a[@id='ap-other-signin-issues-link']")
driver.find_element(By.XPATH, "//a[@id='ap-other-signin-issues-link' and @class='a-link-normal']")
driver.find_element(By.XPATH, "//a[contains(text(),'Other issues with Sign-In')]")


#7.Create your Amazon account button
driver.find_element(By.XPATH, "//a[contains(@href,'register')]")
driver.find_element(By.XPATH, "//a[contains(@href, 'register') and @tabindex='6']")


#8.*Conditions of use link
driver.find_element(By.XPATH, "//a[contains(@href,'footer_cou')]")


#9.*Privacy Notice link
driver.find_element(By.XPATH, "//a[contains(@href,'footer_privacy')]")


