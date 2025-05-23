from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# 3 As: Arrange / Act / Assert

# Arrange (setup)
# init driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
# open the url
driver.get('https://www.target.com/')

# Act
driver.find_element(By.ID, 'search').send_keys('tea')
driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
sleep(5)

# Assert (Verification)
expected_text = 'tea'
actual_text = driver.find_element(By.XPATH, "//div[@data-test='lp-resultsCount']").text

assert expected_text in actual_text, f'Error, expected {expected_text} not in actual {actual_text}'
print('Test case passed')
driver.quit()