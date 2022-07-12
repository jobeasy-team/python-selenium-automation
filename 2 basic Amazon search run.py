from selenium import webdriver
from selenium.webdriver.common.by import By

#initialize driver:
driver = webdriver.Chrome(r"C:\\Users\\ababa\\Desktop\\QA Automation\\PythonSeleniumAutomation\\python-selenium-automation\\chromedriver.exe")
#
#Maximize chrome window
driver.maximize_window()
#
driver.get('https://www.amazon.com')
#
driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('tshirt')
driver.find_element(By.ID, 'nav-search-submit-button').click()
driver.find_element(By.ID, 'twotabsearchtextbox').clear()
driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('YOU MADE IT! IT WORKS HAHAAAAAA')
#
print('TEST SUCCESSFUL')
#
driver.quit()
