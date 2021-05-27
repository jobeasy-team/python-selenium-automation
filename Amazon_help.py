from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome(executable_path='/Users/bkarp0518/Desktop/Automation/python-selenium-automation/chromedriver')
driver.maximize_window()


driver.get('https://www.amazon.com/gp/help/customer/display.html')

driver.find_element(By.ID, 'helpsearch').send_keys("Cancel Order",Keys.RETURN)


assert "Cancel Items or Orders"



