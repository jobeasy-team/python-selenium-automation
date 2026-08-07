from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome()
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

# find el with CSS, ID #
driver.find_element(By.CSS_SELECTOR, '#twotabsearchtextbox')
# tag + id
driver.find_element(By.CSS_SELECTOR, "input#twotabsearchtextbox")
# tag + attr
driver.find_element(By.CSS_SELECTOR, "input[data-agent-field='search-query']")
driver.find_element(By.CSS_SELECTOR, "input[aria-label='Search Amazon']")
driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search Amazon']")

# only att
driver.find_element(By.CSS_SELECTOR, "[placeholder='Search Amazon']")
# multiple attr [][][]...
driver.find_element(By.CSS_SELECTOR, "[tabindex='0'][type='text'][aria-label='Search Amazon']")
driver.find_element(By.CSS_SELECTOR, "input[tabindex='0'][type='text']")

# Using class .
driver.find_element(By.CSS_SELECTOR, "input.nav-progressive-attribute")
# Using multiple class
driver.find_element(By.CSS_SELECTOR, "input.nav-progressive-attribute.nav-input")
driver.find_element(By.CSS_SELECTOR, ".nav-a.icp-link-style-2.nav-a-2")

# Using tag + id + class + attr
driver.find_element(By.CSS_SELECTOR, "input#twotabsearchtextbox.nav-input[role='searchbox']")

# Using class (as an attr) + contains logic *=
driver.find_element(By.CSS_SELECTOR, "div[class*='mobileSearchContainer']")
driver.find_element(By.CSS_SELECTOR, "[data-test*='TargetCircle360']")
