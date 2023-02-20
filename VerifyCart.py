from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# init driver
# driver = webdriver.Chrome(executable_path='C:\\Users\\vsupe\QA\\Automation\\python-selenium-automation\\chromedriver')
service = Service('C:\\Users\\vsupe\QA\\Automation\\python-selenium-automation\\chromedriver')
driver = webdriver.Chrome(service=service)
driver.maximize_window()

#Add one product in the cart
driver.get("https://www.amazon.com/")
driver.find_element(By.ID, "twotabsearchtextbox").send_keys("starbucks coffee")
driver.find_element(By.ID, "nav-search-submit-button").click()
driver.find_element(By.CSS_SELECTOR, 'img.s-image[data-image-index="1"]').click()
driver.find_element(By.ID, 'add-to-cart-button').click()

sleep(3)
#Go to the cart and grab the title of the product and number
driver.find_element(By.CSS_SELECTOR, 'a[href="/gp/cart/view.html?ref_=nav_cart"]').click()
str = driver.find_element(By.CSS_SELECTOR, 'div.a-row span.a-truncate-cut').text
first_word = (str.split())[0]
assert first_word=='Starbucks', f"Item is not added in the cart"

count=0
count = driver.find_element(By.ID, 'nav-cart-count').text
assert count == '1', f"Item is not added in the cart"
print("Test passed")
