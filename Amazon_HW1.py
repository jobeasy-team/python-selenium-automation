''' Locators for sign-in page

Amazon logo (By.XPATH, "//i[@class='a-icon a-icon-logo']")

Coninue button (By.ID, 'continue')

Need help link (By.CLASS, 'a-expander-prompt')

Forgot your password link (By.ID, 'auth-fpp-link-bottom')

Other issues with Sign-In link (By.ID, 'auth-fpp-link-bottom')

Create your Amazon account button  (By.XPATH, "//a[@id='createAccountSubmit']")

*Conditions of use link (By.XPATH, '//a[contains(@href, "signin_notification_condition_of_use")]'
")

*Privacy Notice link (By.XPATH, '//a[contains(@href, "signin_notification_privacy_notice")]'
)
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from time import sleep

# init driver
driver = webdriver.Chrome(executable_path="/Users/victorjefferson/Desktop/python-selenium-automation/chromedriver")
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/gp/help/customer/display.html ')

sleep(4)

search = driver.find_element(By.NAME, 'help_keywords')
search.send_keys('Cancel order')
search.send_keys(Keys.RETURN)

sleep(4)

expected_result = 'Cancel Items or Orders'
actual_result = driver.find_element(By.XPATH, "//a[@class='a-link-normal' and contains(text(), 'Cancel Items')]").text

assert expected_result == actual_result, f'Error, Actual text {actual_result} does not match {expected_result}'
print('Test Case Passed!')

driver.quit()
