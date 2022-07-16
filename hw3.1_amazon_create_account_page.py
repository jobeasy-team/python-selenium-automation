from selenium.webdriver.common.by import By

from sample_script import driver


# Locator for Amazon Label,Using CSS Selector, Class
driver.find_element(By.CSS_SELECTOR, 'i.a-icon-logo')

#Locator for Create account Label, using CSS contains text
driver.find_element(By.XPATH, "//h1[contains(text(),'Create account')")

#Locator for Your name, using CSS ID
driver.find_element(By.CSS_SELECTOR, '#ap_customer_name')

#Locator for mobile number/email, using CSS ID
driver.find_element(By.CSS_SELECTOR, '#ap_email')

#Locator for password, using CSS ID
driver.find_element(By.CSS_SELECTOR, '#ap_password')

#Locator for re-enter password, using CSS ID
driver.find_element(By.CSS_SELECTOR, '#ap_password_check')

#Locator for Continue, using CSS ID
driver.find_element(By.CSS_SELECTOR, '#continue')

#Locator for Conditions of Use, using Xpath,contains
driver.find_element(By.XPATH, "//a[contains(@href,'ap_register_notification_condition_of_use')]")

#Locator for privacy Notice, using Xpath,contains
driver.find_element(By.XPATH, "//a[contains(@href,'ap_register_notification_privacy_notice')]")

#Locator for Sign-In, using CSS, partial href
driver.find_element(By.CSS_SELECTOR, "a[href*='ap/signin?']" )
