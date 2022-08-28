from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome()

# By ID
driver.find_element(By.ID, 'twotabsearchtextbox')

# By CSS, ID
driver.find_element(By.CSS_SELECTOR, '#twotabsearchtextbox')
driver.find_element(By.CSS_SELECTOR, 'input#twotabsearchtextbox')

# By CSS, class(es)
driver.find_element(By.CSS_SELECTOR, 'span.icp-nav-flag-us')
driver.find_element(By.CSS_SELECTOR, 'span.icp-nav-flag.icp-nav-flag-us')
# by class, without a tag
driver.find_element(By.CSS_SELECTOR, '.icp-nav-flag')

# By CSS, attributes
driver.find_element(By.CSS_SELECTOR, "a[href='/gp/help/customer/display.html/ref=ap_signin_notification_condition_of_use?ie=UTF8&nodeId=508088']")
# partial match
driver.find_element(By.CSS_SELECTOR, "a[href*='ap_signin_notification_condition_of_use']")
driver.find_element(By.CSS_SELECTOR, "input[type='email'][name='email'][maxlength='128']")
# mix of ids, classes, attributes:
driver.find_element(By.CSS_SELECTOR, "input#ap_email[type='email']")
driver.find_element(By.CSS_SELECTOR, "input#ap_email.auth-autofocus.a-input-text[type='email']")

# by multiple nodes
driver.find_element(By.CSS_SELECTOR, "ul.hmenu-visible li a[href*='new-releases']")


driver.find_element(By.XPATH, "//div[@class='nav-search-facade' and .//span[@id='nav-search-label-id']]")







