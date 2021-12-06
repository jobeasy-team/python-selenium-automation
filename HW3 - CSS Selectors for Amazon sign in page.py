from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# AMAZON LOGO
driver.find_element(By.CSS_SELECTOR, "i[aria-label='Amazon']")

# CREATE ACCOUNT
driver.find_element(By.CSS_SELECTOR, "h1.a-spacing-small")

# YOUR NAME
driver.find_element(By.CSS_SELECTOR, "#ap_customer_name")

# EMAIL
driver.find_element(By.CSS_SELECTOR, "#ap_email")

# PASSWORD
driver.find_element(By.CSS_SELECTOR, "#ap_password")

# RE-ENTER PASSWORD"
driver.find_element(By.CSS_SELECTOR, "#ap_password_check")

# CONTINUE (CREATE YOUR AMAZON ACCOUNT)
driver.find_element(By.CSS_SELECTOR, "#continue")

# CONDITIONS OF USE
driver.find_element(By.CSS_SELECTOR,
                    "a[href*='/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use']")

# PRIVACY NOTICE
driver.find_element(By.CSS_SELECTOR,
                    "a[href*='/gp/help/customer/display.html/ref=ap_register_notification_privacy_notice']")

# SIGN IN
driver.find_element(By.CSS_SELECTOR, "a[href*='/ap/signin?openid']")
