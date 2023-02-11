from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# init driver
#driver = webdriver.Chrome(executable_path='C:\\Users\\vsupe\QA\\Automation\\python-selenium-automation\\chromedriver')
service = Service('C:\\Users\\vsupe\QA\\Automation\\python-selenium-automation\\chromedriver')
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get("https://www.amazon.com/")
driver.find_element(By.ID, "twotabsearchtextbox").send_keys("almonds")
driver.find_element(By.ID, "nav-search-submit-button").click()
assert "almonds" in driver.current_url.lower(), f'Expected query not present in {driver.current_url.lower()}'
print("Test passed")
