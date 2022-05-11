from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome(executable_path="/Users/victorjefferson/Desktop/python-selenium-automation/chromedriver")
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

search = driver.find_element(By.ID, 'twotabsearchtextbox')
search.send_keys('coffee')
driver.find_element(By.XPATH, "//input[@type='submit']").click()