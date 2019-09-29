from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
# init driver
search = driver = webdriver.Chrome()

# open the url
driver.get('https://www.amazon.com/')

driver.find_element(By.ID, "nav-hamburger-menu").click()
driver.find_element(By.LINK_TEXT, "Help").click()
driver.find_element(By.XPATH, "//input[@class = 'a-input-text a-span12']").send_keys("Cancel orders")
driver.find_element(By.XPATH, "//input[@class = 'a-button-input']").click()

assert "Orders" in driver.find_element(By.XPATH, "//a[@class = 'a-link-normal']").text
driver.quit()





























