from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)

# open the url
driver.get('https://www.target.com/')
sleep(5) # Site sometimes takes longer to load

# Search for a product
driver.find_element(By.ID, 'search').send_keys('tea')
driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()

# Verification:
expected_text = 'tea'
actual_text = driver.find_element(By.XPATH, "//div[@data-test='lp-resultsCount']").text
assert expected_text in actual_text, f'Expected {expected_text} not in actual {actual_text}'

# driver.find_element(By.ID, 'filters-button')
# sleep(5)

