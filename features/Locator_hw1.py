from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(executable_path='/Users/svetlanalevinsohn/JobEasy/13-python-selenium-automation/chromedriver')

#Amazon logo
driver.find_element(By.XPATH, "//i[@aria-label='Amazon']")
#Continue button
driver.find_element(By.XPATH, "//input[@aria-labelledby='continue-announce']")
#Need help link
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")
#Forgot your password link
driver.find_elements(By.XPATH, "//a[contains(@href,'forgotpassword?')]")
#Other issues with Sign-In link
driver.find_element(By.XPATH, "//a[contains(@href,'ap_login_with_otp_claim_collection?')]")
#Create your Amazon account button
driver.find_element(By.XPATH, "//a[contains@href='https://www.amazon.com/ap/register?showRememberMe=true&openid.pape.max_auth_age=0&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&pageId=usflex&mobileBrowserWeblabTreatment=C&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&prevRID=JJNXF8HFZ4JMBW1NAPPH&openid.assoc_handle=usflex&openid.mode=checkid_setup&desktopBrowserWeblabTreatment=C&prepopulatedLoginId=&failedSignInCount=0&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0']")
#Conditions of use link
driver.find_element(By.XPATH, "//a[@href='/gp/help/customer/display.html/ref=ap_signin_notification_condition_of_use?ie=UTF8&nodeId=508088']")
#Privacy Notice link
driver.find_element(By.XPATH, "//a[@href='/gp/help/customer/display.html/ref=ap_signin_notification_privacy_notice?ie=UTF8&nodeId=468496']")



