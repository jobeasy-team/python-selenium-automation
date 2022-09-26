from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Chrome(executable_path="C:/Users/AAA/Desktop/python-selenium-automation/chromedriver.exe")

#Directing to the Signin page

driver.maximize_window()
driver.get('https://www.amazon.com/')
driver.find_element(By.ID, "nav-link-accountList-nav-line-1").click()
#
#
#Locators
#
#
#Logo
driver.find_element(By.XPATH,"//i[@class='a-icon a-icon-logo']")
#Continue Button
driver.find_element(By.ID, "continue")
#Need help link
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']").click()
#Forgot your password link
driver.find_element(By.ID,"auth-fpp-link-bottom" )
#Other issues with Sign-In link
driver.find_element(By.XPATH, "//a[@href='/gp/help/customer/account-issues/ref=ap_login_with_otp_claim_collection?ie=UTF8']")
# Create your Amazon account button
driver.find_element(By.XPATH, "//a[@id='createAccountSubmit' and @tabindex='6']")
#*Conditions of use link
driver.find_element(By.XPATH, "//a[@href= '/gp/help/customer/display.html/ref=ap_signin_notification_condition_of_use?ie=UTF8&nodeId=508088']")




