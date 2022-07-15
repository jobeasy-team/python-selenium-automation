from selenium import webdriver
from selenium.webdriver.common.by import By

#initialize driver:
driver = webdriver.Chrome(r"C:\\Users\\ababa\\Desktop\\QA Automation\\PythonSeleniumAutomation\\python-selenium-automation\\chromedriver.exe")

#Maximize chrome window
driver.maximize_window()
#OPENS WEB PAGE
driver.get('https://www.amazon.com')
#INPUTS KEYS/WORDS INTO A FIELD
driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('tshirt')
#CLICK
driver.find_element(By.ID, 'nav-search-submit-button').click()
#CLEARS INPUT FIELD
driver.find_element(By.ID, 'twotabsearchtextbox').clear()

driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('YOU MADE IT! IT WORKS HAHAAAAAA')

print('TEST SUCCESSFUL')
#EXIT BROWSER
driver.quit()
