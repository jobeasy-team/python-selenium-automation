from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# init driver
driver = webdriver.Chrome()
driver.maximize_window()

# open the url
driver.get("https://www.google.com")

# wait
wait = WebDriverWait(driver, 10)

# find search box and enter text
search = wait.until(EC.presence_of_element_located((By.NAME, "q")))
search.send_keys("Dress")
search.send_keys(Keys.RETURN)   # better than clicking button

# wait for results page
wait.until(EC.url_contains("dress"))

# verify
assert "dress" in driver.current_url.lower(), f"Expected query not in {driver.current_url.lower()}"
print("Test Passed")

driver.quit()
