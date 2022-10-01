from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='/Users/svetlanalevinsohn/JobEasy/12-python-selenium-automation/chromedriver')

# By tag & ID
driver.find_element(By.CSS_SELECTOR, "input#twotabsearchtextbox")
# By ID
driver.find_element(By.CSS_SELECTOR, "#twotabsearchtextbox")
driver.find_element(By.ID, "twotabsearchtextbox")

# By class
driver.find_element(By.CSS_SELECTOR, ".icp-nav-flag-us")
# By multiple classes
driver.find_element(By.CSS_SELECTOR, ".icp-nav-flag-us.icp-nav-flag")
# By class + tag
driver.find_element(By.CSS_SELECTOR, "span.icp-nav-flag-us.icp-nav-flag")

# By attribute:
driver.find_element(By.CSS_SELECTOR, "input[name='email']")
driver.find_element(By.CSS_SELECTOR, "[name='email']")
driver.find_element(By.CSS_SELECTOR, "[href='/gp/help/customer/display.html/ref=ap_signin_notification_condition_of_use?ie=UTF8&nodeId=508088']")
# By multiple attributes:
driver.find_element(By.CSS_SELECTOR, "input[name='email'][type='email'][maxlength='128']")
# By attribute + class
driver.find_element(By.CSS_SELECTOR, "input.a-button-input[type='submit']")
driver.find_element(By.CSS_SELECTOR, "input.a-button-input.class[type='submit'][]")
driver.find_element(By.CSS_SELECTOR, ".a-button-input.class[type='submit'][]")
# By partial attribute
driver.find_element(By.CSS_SELECTOR, "a[href*='ap_signin_notification_condition_of_use']")
# For classes, to get partial match:
driver.find_element(By.CSS_SELECTOR, "a[class*='button']")

# From parent => child
driver.find_element(By.CSS_SELECTOR, "div#legalTextRow a[href*='condition']")

# Xpath backwards (from child to parent)
driver.find_element(By.XPATH, "//*[./a[contains(@href, 'signin_notification_condition_of_use')]]")