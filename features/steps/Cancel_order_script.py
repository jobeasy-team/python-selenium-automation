from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path='/Users/bkarp0518/Desktop/Automation/python-selenium-automation/chromedriver')
driver.maximize_window()


driver.get('https://www.amazon.com/gp/help/customer/display.html')

driver.find_element(By.ID, 'helpsearch').send_keys("Cancel Order",Keys.RETURN)
actual_text = driver.find_element(By.XPATH, "//div[@class='help-content']/h1").text
expected_result = 'Cancel Items or Orders'

assert expected_result == actual_text, f'Expected {expected_result}, but got {actual_text}'

driver.quit()






