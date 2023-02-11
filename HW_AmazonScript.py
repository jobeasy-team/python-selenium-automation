from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# init driver
#driver = webdriver.Chrome(executable_path='C:\\Users\\vsupe\QA\\Automation\\python-selenium-automation\\chromedriver')
service = Service('C:\\Users\\vsupe\QA\\Automation\\python-selenium-automation\\chromedriver')
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get("https://www.amazon.com/")
driver.find_element(By.ID, 'nav-orders').click()

#Check if "Sign in" text is present
expected_text = "Sign in"
actual_text = driver.find_element(By.XPATH, "//h1[contains(text(),'Sign in')]").text
assert expected_text == actual_text, f'Expected {expected_text} but got {actual_text}'

#Check if Email input field is present
expected_label = 'Email or mobile phone number'
actual_label = driver.find_element(By.ID, 'ap_email').accessible_name
assert expected_label == actual_label, f'Expected Email input field is not present on the Sign in page'

print("Test case passed")

driver.close()
