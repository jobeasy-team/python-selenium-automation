from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome(executable_path='C:\\Users\\vsupe\QA\\Automation\\python-selenium-automation\\chromedriver')
driver.maximize_window()
# open the url
driver.get('https://www.amazon.com/')
#Amazon image using a class
driver.find_element(By.CSS_SELECTOR, 'i.a-icon.a-icon-logo')

#Create account Label by parent->child
driver.find_element(By.CSS_SELECTOR, 'div.a-box.a-spacing-extra-large div.a-box-inner h1.a-spacing-small')

#Your name input field using id
driver.find_element(By.CSS_SELECTOR, '#ap_customer_name')

#Email input field using multiple classes
driver.find_element(By.CSS_SELECTOR, 'input.a-input-text.a-span12.a-spacing-micro.auth-required-field.auth-require-claim-validation')

#Password input field using class+attributes
driver.find_element(By.CSS_SELECTOR, 'input.a-input-text[type=password][name="password"]')

#Re-enter password input field using class+attributes
driver.find_element(By.CSS_SELECTOR, 'input.a-input-text[name="passwordCheck""]')

#Create your amazon account button
driver.find_element(By.CSS_SELECTOR, 'input#continue')

#Conditions of use link using parent->child and contains
driver.find_element(By.CSS_SELECTOR, 'div#legalTextRow a[href*="ie=UTF8&nodeId=508088"]')

#Privacy notice link using parent->child and contains
driver.find_element(By.CSS_SELECTOR, 'div#legalTextRow a[href*="ie=UTF8&nodeId=468496"]')

#Sign in link using class and attributes
driver.find_element(By.CSS_SELECTOR, 'a.a-link-emphasis[href*="signin"]')





