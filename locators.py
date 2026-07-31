from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome()
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

# By ID
driver.find_element(By.ID, 'twotabsearchtextbox')

# By XPATH
driver.find_element(By.XPATH, "//input[@placeholder='Search Amazon']")
# multiple attributes
driver.find_element(By.XPATH, "//input[@type='text' and @aria-label='Search Amazon']")

# any tag, use * :
driver.find_element(By.XPATH, "//*[@type='text' and @aria-label='Search Amazon']")
driver.find_element(By.XPATH, "//*[@placeholder='Search Amazon']")

# text() (note, text is not an attr)
driver.find_element(By.XPATH, "//a[text()='Health AI']")

# XPATH, contains()
driver.find_element(By.XPATH, "//a[@href='https://health.amazon.com/health-ai?ref_=nav_cs_health_ai']") # =>
driver.find_element(By.XPATH, "//a[contains(@href, 'nav_cs_health_ai')]")
driver.find_element(By.XPATH, "//span[contains(text(), 'Summer fitness')]")

# XPATH, from parent => child node
driver.find_element(By.XPATH, "//div[@id='nav-xshop']//a[text()='Best Sellers']")




