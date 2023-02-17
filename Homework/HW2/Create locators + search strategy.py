from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.service import
from sample_script import driver

#Amazon Logo
driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']")

#Continue Button
driver.find_element(By.ID, 'continue')

#Need help link
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")

#Forgot your password link
driver.find_element(By.XPATH, "//a[contains(text(),'Forgot your password?')]")

#Other issues with Sign-In link
driver.find_element(By.ID, 'ap-other-signin-issues-link')

#Create your Amazon account button
driver.find_element(By.ID, 'createAccountSubmit')

#Conditions of use link
driver.find_element(By.XPATH, "//a[contains(text(), 'Conditions of Use') and contains(@herf, 'ap_signin_notification_condition_of_use')]")

#Privacy Notice link
driver.find_element(By.XPATH, "//a[contains(text(), 'Privacy Notice') and contains(@herf, 'ap_signin_notification_privacy_notice?ie=UTF8&nodeId=468496')]")
