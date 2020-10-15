from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome('../../drivers/chromedriver_win32/chromedriver.exe')
driver.maximize_window()

# open the url
driver.get('https://www.google.com/')

search = driver.find_element(By.NAME, 'q')
search.clear()
search.send_keys('watches')

# wait for 4 sec
sleep(4)

# click search
driver.find_element(By.NAME, 'btnK').click()

print("START")
print(driver.find_element(By.XPATH, "//div[@class='g']").text)
print("STOP")
# verify
#assert 'watches' in driver.find_element(By.XPATH, "//div[contains(@class,'commercial-unit-desktop-top')]").text
#assert 'watches' in driver.find_element(By.XPATH, "//div[@class='g']").text

#driver.quit()
