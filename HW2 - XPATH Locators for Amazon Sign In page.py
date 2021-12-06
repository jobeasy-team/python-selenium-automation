from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# Create locators + search strategy for these page elements of Amazon Sign in page:
# For example: Email field, search by ID, “ap_email”

# 1.Amazon logo
# By contains..."a-icon a-icon-logo"
driver.find_element(By.XPATH, "//i[contains(@class,'a-icon a-icon-logo')]")

# 2.Email field
# By ID..."ap_email"
driver.find_element(By.XPATH, "//input[@id='ap_email']")

# 3.Continue button
# By multiple attributes...tabindex and class
driver.find_element(By.XPATH, "//input[@tabindex='5' and @class='a-button-input']")

# 4.Need help link
# By XPATH...span tag class attribute
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")

# 5.Forgot your password link
# By Contains 'forgotyourpassword'
driver.find_element(By.XPATH, "//a[contains(@href, 'forgotyourpassword?')]")
# Note to Svetlana: I used same method given in the video. Why it shows "[]length: 0[[Prototype]]: Array(0)" in Chrome Console?

# 6.Other issues with Sign-In link
# By multiple attributes...ID and class
driver.find_element(By.XPATH, "//a[@id='ap-other-signin-issues-link' and @class='a-link-normal']")

# 7.Create your Amazon account button
# By multiple attributes, contains for partial attributes
driver.find_element(By.XPATH, "//a[contains(@href, 'register') and @tabindex='6']")

# 8.*Conditions of use link
# By XPATH
driver.find_element(By.XPATH,
                    "//a[@href='/gp/help/customer/display.html/ref=ap_desktop_footer_cou?ie=UTF8&nodeId=508088']")

# 9.*Privacy Notice link
# By XPATH
driver.find_element(By.XPATH,
                    "//a[@href='/gp/help/customer/display.html/ref=ap_desktop_footer_privacy_notice?ie=UTF8&nodeId=468496']")
