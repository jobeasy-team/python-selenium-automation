from selenium import webdriver
from selenium.webdriver.common.by import By


#1. Find the most optimal locators for Create Account (Registration) page elements:

driver= webdriver.Chrome(executable_path= 'C:/Users/AAA/Desktop/python-selenium-automation/chromedriver.exe')
driver.get('https://www.amazon.com/ap/register?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3F_encoding%3DUTF8%26ref_%3Dnav_newcust&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&')


# Amazon logo
driver.find_element(By.XPATH, "//i[@class ='a-icon a-icon-logo']")

#Create account

driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']")

# Your Name box
driver.find_element(By.ID, "ap_customer_name")

# Mobile number or email box
driver.find_element(By.ID, "ap_email")

#Password box
driver.find_element(By.ID, "ap_password")

#Re-enter password
driver.find_element(By.ID, "ap_password_check")

#Continue button
driver.find_element(By.ID, "continue")

#Condition of Use link
driver.find_element(By.XPATH, "//a[@href= 'https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_privacy_notice?ie=UTF8&nodeId=468496']")

#Privacy Notice link
driver.find_element(By.XPATH, "//a[contains(@href, 'html/ref=ap_register_notification_privacy_notice')]")

#Sign in link
driver.find_element(By.XPATH, "//a[contains(@href, 'https://www.amazon.com/ap/signin?)]")
