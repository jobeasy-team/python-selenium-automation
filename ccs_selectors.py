from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.service import Service

# driver = webdriver.Chrome(executable_path='/Users/svetlanalevinsohn/JobEasy/13-python-selenium-automation/chromedriver')
service = Service('/Users/svetlanalevinsohn/JobEasy/13-python-selenium-automation/chromedriver')
driver = webdriver.Chrome(service=service)

# by ID
driver.find_element(By.ID, 'twotabsearchtextbox')
driver.find_element(By.ID, 'ap_customer_name')
driver.find_element(By.ID, 'ap_email')


# By CSS, using ID Syntax tag#ID but you can omit tag. instead of  'input#twotabsearchtextbox'use '#twotabsearchtextbox'
driver.find_element(By.CSS_SELECTOR, '#twotabsearchtextbox')
driver.find_element(By.CSS_SELECTOR, '#ap_customer_name')
driver.find_element(By.CSS_SELECTOR, '#ap_email')
driver.find_element(By.CSS_SELECTOR, '#ap_password')
driver.find_element(By.CSS_SELECTOR, '#ap_password_check')
driver.find_element(By.CSS_SELECTOR, '#continue')
driver.find_element(By.CSS_SELECTOR, '#ab-registration-link')


# By class - Syntax tag.class You can omit tag --> .class
driver.find_element(By.CSS_SELECTOR, ".icp-nav-flag-us")
driver.find_element(By.CSS_SELECTOR, ".a-icon-logo")
driver.find_element(By.CSS_SELECTOR, ".a-spacing-small")
# By multiple classes Syntax .class.class --> classes are separated by dot .
driver.find_element(By.CSS_SELECTOR, ".icp-nav-flag-us.icp-nav-flag")
# By tag + multiple classes Syntax tag.class.class
driver.find_element(By.CSS_SELECTOR, "span.icp-nav-flag-us.icp-nav-flag")

# By CSS using attributes (except ID and class see syntax for it above) Syntax tag[attribute='value']
driver.find_element("a[href='/gp/bestsellers/?ref_=nav_cs_bestsellers']")
driver.find_element("a[data-csa-c-content-id='nav_cs_bestsellers']")
driver.find_element(By.CSS_SELECTOR, "input[name='email']")
driver.find_element(By.CSS_SELECTOR, "[name='email']")
driver.find_element(By.CSS_SELECTOR, "[href='/gp/help/customer/display.html/ref=ap_signin_notification_condition_of_use?ie=UTF8&nodeId=508088']")
# By multiple attributes, Syntax tag[attribute='value'][attribute='value']
driver.find_element(By.CSS_SELECTOR, "input[name='email'][type='email'][maxlength='128']")
driver.find_element(By.CSS_SELECTOR, "a[href='/music/unlimited?ref_=nav_cs_music'][data-csa-c-content-id='nav_cs_music']"
# By attribute + class Syntax tag.class[attribute='value']
driver.find_element(By.CSS_SELECTOR, "a.nav-a[data-csa-c-content-id='nav_cs_books']"
driver.find_element(By.CSS_SELECTOR, "input.a-button-input[type='submit']")
driver.find_element(By.CSS_SELECTOR, "input.a-button-input.class[type='submit'][]")
driver.find_element(By.CSS_SELECTOR, ".a-button-input.class[type='submit'][]")

# By partial attribute Syntax tag[attribute*='']
driver.find_element(By.CSS_SELECTOR, "a[href*='ap_signin_notification_condition_of_use']"
driver.find_element(By.CSS_SELECTOR, "a[href*='ap_register_notification_condition_of_use']")
driver.find_element(By.CSS_SELECTOR, "a[href*='ap_register_notification_privacy_notice']")

# By class and partial attribute Syntax tag.class[attribute*='partial_value']
driver.find_element(By.CSS_SELECTOR, "a.a-link-emphasis[href*='ap/signin?showRmrMe']")

# For classes, to get partial match (use *):
driver.find_element(By.CSS_SELECTOR, "a[class*='button']")

# From parent => child Syntax tag#id_value tag[attribute*='value']
driver.find_element(By.CSS_SELECTOR, "div#legalTextRow a[href*='condition']")
driver.find_element(By.CSS_SELECTOR, "div#legalTextRow a[href*='ap_register_notification_condition_of_use']")
driver.find_element(By.CSS_SELECTOR, "div#legalTextRow a[href*='ap_register_notification_privacy_notice']")




