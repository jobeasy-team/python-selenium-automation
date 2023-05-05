from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# driver = webdriver.Chrome(executable_path='/Users/ekaterinasuvorova/Automation2023/python-selenium-automation/chromedriver')
service = Service('/Users/ekaterinasuvorova/Automation2023/python-selenium-automation/chromedriver')
driver = webdriver.Chrome(service=service)


# By ID
driver.find_element(By.ID, 'twotabsearchtextbox')
driver.find_element(By.ID, 'nav-link-accountList')
driver.find_element(By.ID, 'continue')
driver.find_element(By.ID, 'createAccountSubmit')

# By Xpath, tag and attribute
driver.find_element(By.XPATH, "//input[@placeholder='Search Amazon']")
driver.find_element(By.XPATH, "//input[@aria-label='Search Amazon']")
driver.find_element(By.XPATH, "//img[@alt='PAVOI Jewelry']")
driver.find_element(By.XPATH, "//i[@aria-label='Amazon']")
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")

# By Xpath, multiple attributes
driver.find_element(By.XPATH, "//a[@aria-label='Amazon' and @href='/ref=nav_logo']")
driver.find_element(By.XPATH, "//a[@href='/gp/bestsellers/?ref_=nav_cs_bestsellers' and @data-csa-c-content-id='nav_cs_bestsellers' and @data-csa-c-type='link']")



# By Xpath, contains:
driver.find_element(By.XPATH, "//a[contains(@href, 'nav_cs_bestsellers')]")
# contains AND attr
driver.find_element(By.XPATH, "//a[contains(@href, 'bestsellers') and @data-csa-c-type='link']")

# By Xpath, without a tag
driver.find_element(By.XPATH, "//*[contains(@href, 'bestsellers') and @data-csa-c-type='link']")
driver.find_element(By.XPATH, "//*[@aria-label='Search Amazon']")
driver.find_element(By.XPATH, "//*[contains(@href, 'ap_signin_notification_condition_of_use')]")
driver.find_element(By.XPATH, )
driver.find_element(By.XPATH, "//*[contains(@href, 'ap_signin_notification_privacy_notice')]")



# By xpath, attr starts with certain value:
driver.find_element(By.XPATH, '//a[starts-with(@href, "/gp/bestsellers/?")]')

# By xpath, text
driver.find_element(By.XPATH, "//h2[text()='The warm-weather edit']")
# Contains text:
driver.find_element(By.XPATH, "//h2[contains(text(), 'The warm-weather')]")
driver.find_element(By.XPATH, "//a[text()='Best Sellers' and @class='nav-a  ']")

# By xpath, going from parent node ==> child
driver.find_element(By.XPATH, "//div[@id='nav-xshop']//a[text()='Best Sellers']")
driver.find_element(By.XPATH, "//div[@id='legalTextRow']//a[text()='Conditions of Use']")