from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='C:/Users/Анна/Desktop/Selenium/python-selenium-automation/chromedriver.exe')
driver.get('https://www.amazon.com/gp/help/customer/display.html')

driver.find_element(By.ID, 'helpsearch').send_keys('cancel_order')

search = driver.find_element(By.ID, "helpsearch")
search.clear()
search.send_keys('cancel order', Keys.ENTER)

