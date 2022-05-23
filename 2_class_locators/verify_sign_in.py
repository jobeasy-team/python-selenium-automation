from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(
    executable_path="C:/ProgramData/Microsoft/Windows/Start Menu/Programs/JetBrains/chromedriver.exe")
driver.get("https://www.amazon.com/")

var = driver.find_element(By.XPATH, "//span[text()='& Orders']").click()







