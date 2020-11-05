from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


BTN = (By.NAME, 'btnK')
# init driver
driver = webdriver.Chrome('../../drivers/chromedriver_win32/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(4) #passed once to browser

# open the url
driver.get('https://www.google.com/')

search = driver.find_element(By.NAME, 'q')
search.clear()
search.send_keys('watches')

# wait for 4 sec
#sleep(4)

# click search
driver.wait = WebDriverWait(driver, 10)
driver.wait.untill(EC.element_to_be_clickable(BTN)).click()
#driver.find_element(By.NAME, 'btnK').click()

print("START")
print(driver.find_element(By.XPATH, "//div[@class='g']").text)
print("STOP")
# verify
assert 'watches' in driver.find_element(By.XPATH, "//div[contains(@class,'commercial-unit-desktop-top')]").text
assert 'watches' in driver.find_element(By.XPATH, "//div[@class='g']").text

driver.quit()
