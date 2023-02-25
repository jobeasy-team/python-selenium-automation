from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.service import
from sample_script import driver

#Amazon Logo
driver.find_element(By.CSS_SELECTOR, 'i.a-icon-logo')

#Create Account
driver.find_element(By.CSS_SELECTOR, 'h1.a-spacing-small')

#Your Name
driver.find_element(By.CSS_SELECTOR, '#ap_customer_name')

#Mobile Number or Email
driver.find_element(By.CSS_SELECTOR, '#ap_email')

#Password
driver.find_element(By.CSS_SELECTOR, '#ap_password')

#Re-enter Password
driver.find_element(By.CSS_SELECTOR, '#ap_password_check')

#Continue
driver.find_element(By.CSS_SELECTOR, '#continue')

#Conditions of Use
driver.find_element(By.CSS_SELECTOR, "a[href*='/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=5080']")

#Privacy Notice
driver.find_element(By.CSS_SELECTOR, "a[href*='/gp/help/customer/display.html/ref=ap_register_notification_privacy_notice?ie=UTF8&nodeId=4684']")

#Sign In
driver.find_element(By.CSS_SELECTOR, "a[class*='/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fwelcomeomletter%2Fb%2F%3F_encoding%3DUTF8%26node%3D86386266011%26ref_%3Dnav_ya_signin%26pd_rd_w%3Dh9Ixi%26content-id%3Damzn1.sym.9ff997c9-ac5a-4385-a402-8b0e23a9d54a%26pf_rd_p%3D9ff997c9-ac5a-4385-a402-8b0e23a9d54a%26pf_rd_r%3DYQH635K8KMWSNJRP03ZF%26pd_rd_wg%3Dg7Q33%26pd_rd_r%3Dd830e944-36af-472d-9685-d172c953ee1d&prevRID=H2DQN7C49DZYEW28XDED&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&failedSignInCount=0&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&pageId=usflex&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0']")

