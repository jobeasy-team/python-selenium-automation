from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path="C:\ProgramData\Microsoft\Windows\Start Menu\Programs\JetBrains\chromedriver.exe")
driver.get("https://www.amazon.com")
#  Find the most optimal locators for Create Account (Registration) page elements


# Amazon logo
driver.find_element(By.CSS_SELECTOR, 'i.class="a-icon.a-icon-logo')

# creat account
driver.find_element(By.CSS_SELECTOR, 'h1.a-spacing-small')

# your name
driver.find_element(By.XPATH, "//label[@class='a-form-label' and @for='ap_customer_name']")

# email
driver.find_element(By.XPATH,"//label[contains(@class,'a-form-label') and @for='ap_email']")

# password
driver.find_element(By.ID, 'ap_password')

# re enter your password
driver.find_element(By.ID, 'ap_password_check')

# Creat (continue) your amazon account button

driver.find_element(By.ID, 'continue')

# condition and policy
driver.find_element(By.ID, 'legalTextRow')

# sign in button
driver.find_element(By.XPATH, "//a[contains(@href,'signin?openid.pape.max_auth')]")


