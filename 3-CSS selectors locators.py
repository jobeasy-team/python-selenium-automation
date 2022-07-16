from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(r"C:\\Users\\ababa\\Desktop\\QA Automation\\PythonSeleniumAutomation\\python-selenium-automation\\chromedriver.exe")


#AMAZON LOCATORS
#1.Amazon logo:
driver.find_element(By.CSS_SELECTOR, 'i.a-icon.a-icon-logo')


#2.Create Account:
driver.find_element(By.CSS_SELECTOR, 'h1.a-spacing-small')


#3.Your Name:
driver.find_element(By.CSS_SELECTOR, '#ap_customer_name')


#4.Email:
driver.find_element(By.CSS_SELECTOR, 'input#ap_email')


#5.Password:
driver.find_element(By.CSS_SELECTOR, '#ap_password')


#6.Re-enter password:
driver.find_element(By.CSS_SELECTOR, '#ap_password_check')


#7.Create Amazon Account (changed to "CONTINUE"):
driver.find_element(By.CSS_SELECTOR, '#continue')
driver.find_element(By.CSS_SELECTOR, "[tabindex='8'][type='submit']")


#8.Conditions of Use:
driver.find_element(By.CSS_SELECTOR, "a[href*='condition_of_use']")


#9.Privacy Notice:
driver.find_element(By.CSS_SELECTOR, "a[href*='notification_privacy_notice']")


#10.Sign in:
driver.find_element(By.CSS_SELECTOR, "a.a-link-emphasis[href*='signin']")


