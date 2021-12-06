from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
#AMAZON LOGO
driver.find_element(By.CSS_SELECTOR, "i[aria-label='Amazon']")

