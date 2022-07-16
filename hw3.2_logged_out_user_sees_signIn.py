from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


# init driver
driver = webdriver.Chrome(executable_path='C:\\Users\\tosha\\Automation\\python-selenium-automation\\chromedriver')
driver.maximize_window()

#Launching the URL
driver.get('https://www.amazon.com/')

sleep(2)
#Clicking the orders Link
driver.find_element(By.XPATH, "//a[@id='nav-orders' and @href='/gp/css/order-history?ref_=nav_orders_first']").click()

#Asserting navigation to signinPage
assert 'signin' in driver.current_url.lower(), f"Expected query not in {driver.current_url.lower()}"
print('Sign text found in URL: Test Passed')

#Asserting Signin Text is present on the input form
signIn_text = driver.find_element(By.XPATH, "//h1[contains(text(),'Sign-In')]").text
sleep(2)
assert 'Sign-In' in signIn_text, f"Expected query not in {signIn_text}"
print('signIn Text is present:Test Passed')
