from selenium import webdriver
from selenium.webdriver.common.by import By
driver= webdriver.Chrome(executable_path='C:/Users/AAA/Desktop/python-selenium-automation/chromedriver.exe')

driver.find_element(By.XPATH,"//tagname[@attribute='']" )