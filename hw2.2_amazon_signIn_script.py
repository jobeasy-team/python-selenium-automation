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
print('Test Passed')

#Asserting Signin Text is present
signIn_text = driver.find_element(By.XPATH, "//h1[contains(text(),'Sign-In')]").text
sleep(2)
assert 'Sign-In' in signIn_text, f"Expected query not in {signIn_text}"
print('signIn Text is present')


#Asserting Email as input field is present
email_field_type = driver.find_element(By.XPATH, "//input[@id='ap_email']").get_attribute('type')

sleep(2)
assert 'email' in email_field_type,f"Expected query not in {email_field_type}"
print('Email Input field  is present')

#Asserting Email Text is present
email_text = driver.find_element(By.XPATH, "//label[contains(text(),'Email or')]").is_displayed()
sleep(2)
#assert 'Email' in email_text, f"Expected query not in {email_text}"// @svetlana : can you please explain why this line was giving me a boolean error?
print('Email Text is present as header for input box')


driver.quit()





