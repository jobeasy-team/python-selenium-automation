from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='C:/Users/Анна/Desktop/Selenium/python-selenium-automation/chromedriver.exe')

driver.get('https://www.amazon.com/gp/help/customer/display.html')

search = driver.find_element(By.ID, 'helpsearch')
search.clear()
search.send_keys('Cancel order', Keys.ENTER)

actual_text = driver.find_element(By.XPATH, "//div[@class='help-content]/h1").text
expected_text = 'Cancel Itens or Orders'

assert expected_text ==actual_text, f'Expected{expected_text} does not match {actual_text}'

driver.quit()