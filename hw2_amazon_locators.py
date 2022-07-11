'''## HW2 -- Practice With Amazon Sign In Page Locators

# Amazon Logo
driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']")

#Continue Button
driver.find_element(By. ID, "//input[@id='continue']")

#Need Help
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")

#help
driver.find_element(By.XPATH,"//a[@href='help']")

#Privacy Notice link (Xpath and Text)
driver.find_element(By.XPATH,"//a[text()='Privacy Notice']")

#Conditions of Use (Xpath and Text)
driver.find_element(By.XPATH, "//a[text()='Conditions of Use']")

#Create your amazon account
driver.find_element(By.ID,"//a[@id='createAccountSubmit']")

'''







