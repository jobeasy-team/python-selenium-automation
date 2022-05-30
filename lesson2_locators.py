from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='/Users/jemitpatel/Automation/python-selenium-automation/chromedriver')
driver.get('https://www.amazon.com/')

# By ID
driver.find_element(By.ID, 'twotabsearchtextbox')

# By XPath
driver.find_element(By.XPATH, "//a[@href='/ref=nav_logo']")
driver.find_element(By.XPATH, "//a[@class='nav-logo-link nav-progressive-attribute']")
driver.find_element(By.XPATH, "//a[@aria-label='Amazon']")

# By XPath, 2 attributes 'and'
driver.find_element(By.XPATH, "//a[@class='nav-a  ' and @data-csa-c-content-id='nav_cs_bestsellers']")

# By partial attribute
driver.find_element(By.XPATH, "//a[contains(@href, 'nav_cs_bestsellers')]")

# By XPath, by text
driver.find_element(By.XPATH, "//a[text()='Best Sellers']")
driver.find_element(By.XPATH, "//span[text()='Help the people of Ukraine.']")

# By XPath, partial text
driver.find_element(By.XPATH, "//span[contains(text(), 'the people of Ukraine')]")

# By XPath, only attribute or text, no tag
driver.find_element(By.XPATH, "//*[text()='Help the people of Ukraine.']")
driver.find_element(By.XPATH, "//*[@data-csa-c-content-id='nav_cs_bestsellers']")

# By XPath, using multiple nodes
driver.find_element(By.XPATH, "//div[@id='nav-xshop-container']//a[text()='Best Sellers']")
