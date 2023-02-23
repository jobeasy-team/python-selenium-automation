from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(executable_path='/Users/jj/python-selenium-automation/chromedriver_mac_arm64')

# By ID
driver.find_element(By.ID, 'twotabsearchtextbox')

# By CSS, using ID
driver.find_element(By.CSS_SELECTOR, '#twotabsearchtextbox')

# By CSS, using class
driver.find_element(By.CSS_SELECTOR, 'span.icp-nav-flag-lop')
driver.find_element(By.CSS_SELECTOR, '.icp-nav-flag-lop')
# multiple classes =>
driver.find_element(By.CSS_SELECTOR, 'span.icp-nav-flag-us.icp-nav-flag-lop.icp-nav-flag')

# By CSS, using attributes (except ID amd Class)
driver.find_element(By.CSS_SELECTOR, "a[data-csa-c-content-id='nav_cs_bestsellers']")
driver.find_element(By.CSS_SELECTOR, "a[href='/gp/bestsellers/?ref_=nav_cs_bestsellers']")
# multiple attr
driver.find_element(By.CSS_SELECTOR, "a[data-csa-c-content-id='nav_cs_bestsellers'][tabindex='0']")

# class + attr
driver.find_element(By.CSS_SELECTOR, "a.nav-a[data-csa-c-content-id='nav_cs_bestsellers'][tabindex='0']")
driver.find_element(By.CSS_SELECTOR, "a.[]")

# Attributes, partial match *=
driver.find_element(By.CSS_SELECTOR, "a[href*='?ref_=nav_cs_bestsellers']")

# CSS, from parent to child
driver.find_element(By.CSS_SELECTOR, "#legalTextRow a[href*=condition_of_use]")
driver.find_element(By.CSS_SELECTOR, "div.a-section #legalTextRow a[href*=condition_of_use]")


# XPATH backwards (from child up to parent)
driver.find_element(By.XPATH, "//*[./a[contains(@href, 'ap_signin_notification_condition_of_use')]]")
