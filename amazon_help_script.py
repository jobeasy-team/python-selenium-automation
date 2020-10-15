from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# init driver
driver = webdriver.Chrome('../../drivers/chromedriver_win32/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)

# open the url
driver.get(' https://www.amazon.com/gp/help/customer/display.html ')

input_field = driver.find_element(By.ID, 'helpsearch').send_keys('Cancel order',Keys.ENTER)
sleep(4)
result = driver.find_element(By.XPATH, "//h1[text()='Cancel Items or Orders']")
assert result.text == "Cancel Items or Orders", f'Error.Expected Cancel Items or Orders, but got(result.text)'

driver.quit()
