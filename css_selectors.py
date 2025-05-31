from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

driver.find_element(By.ID, 'twotabsearchtextbox')
# by css, ID
driver.find_element(By.CSS_SELECTOR, '#twotabsearchtextbox')
# ID + tag
driver.find_element(By.CSS_SELECTOR, 'input#twotabsearchtextbox')
# by class
driver.find_element(By.CSS_SELECTOR, '.nav-a')
driver.find_element(By.CSS_SELECTOR, '.nav-logo-link')
driver.find_element(By.CSS_SELECTOR, '.nav-a-2.icp-link-style-2')
driver.find_element(By.CSS_SELECTOR, '.nav-a-2.icp-link-style-2.nav-a')
# by tag + class
driver.find_element(By.CSS_SELECTOR, 'a.nav-logo-link.nav-progressive-attribute')
# by tag + id + class
driver.find_element(By.CSS_SELECTOR, 'a#nav-logo-sprites.nav-logo-link.nav-progressive-attribute')
# by attribute
driver.find_element(By.CSS_SELECTOR, '[aria-label="Amazon"]')
# by tag + attribute
driver.find_element(By.CSS_SELECTOR, 'a[aria-label="Amazon"]')
driver.find_element(By.CSS_SELECTOR, '[lang="en"][aria-label="Amazon"]')
driver.find_element(By.CSS_SELECTOR, '[lang="en"][aria-label="Amazon"]')
# tag + id + class + attributes
driver.find_element(By.CSS_SELECTOR, 'a#nav-logo-sprites.nav-logo-link[lang="en"][aria-label="Amazon"]')

# By using attribute partial match, use *=
driver.find_element(By.CSS_SELECTOR, "[href*='ap_signin_notification_condition_of_use']")
driver.find_element(By.CSS_SELECTOR, "[class*='styles_ndsScreenReaderOnly'][class*='styles_notFocusable']")

# TODO: 10 min break :)



