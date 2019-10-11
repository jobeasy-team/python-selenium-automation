from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome()

# open the url
driver.get('https://www.amazon.com')
sleep(1)

# click Try Prime
driver.find_element(By.XPATH, "//a[@id = 'nav-link-prime']/span[@class = 'nav-line-2 ']").click()
sleep(1)

driver.find_element(By.XPATH, "//div[@class='prime-button-try']/a").click()
sleep(3)

assert "https://www.amazon.com/amazonprime" in driver.current_url

driver.quit()
