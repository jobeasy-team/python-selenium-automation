from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

# Locators:
# By ID, preferred way of locating elements
driver.find_element(By.ID, 'twotabsearchtextbox')

# By XPath
driver.find_element(By.XPATH, "//input[@placeholder='Search Amazon']")
driver.find_element(By.XPATH, "//input[@role='searchbox']")

# By XPath, any tag
driver.find_element(By.XPATH, "//*[@placeholder='Search Amazon']")

# By XPath, combination of attributes
driver.find_element(By.XPATH, "//input[@tabindex='0' and @name='field-keywords' and @spellcheck='false']")
driver.find_element(By.XPATH, "//*[@tabindex='0' and @name='field-keywords' and @spellcheck='false']")
driver.find_element(By.XPATH, "//input[@name='field-keywords' and @tabindex='0' and @spellcheck='false']")

# by text
driver.find_element(By.XPATH, "//a[text()='Best Sellers']")
driver.find_element(By.XPATH, "//a[text()='Best Sellers' and @class='nav-a  ']")

# partial match
driver.find_element(By.XPATH, "//a[contains(@href, 'ref_=nav_cs_bestsellers')]")

# parent => child nodes
driver.find_element(By.XPATH, "//div[@id='navbar']//a[text()='Best Sellers']")

