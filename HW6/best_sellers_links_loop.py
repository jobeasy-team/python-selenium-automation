from time import sleep
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC

BEST_SELLERS_LINK = (By.CSS_SELECTOR, 'a[href*="/gp/bestsellers"]')
LINKS = (By.CSS_SELECTOR, 'div._p13n-zg-nav-tab-all_style_zg-tabs__EYPLq li')

@when('Click on Best Sellers link on the top menu')
def click_on_bestsellers_link(context):
    context.driver.find_element(*BEST_SELLERS_LINK).click()


@then('Clicks on each top link and Verifies that correct page opens')
def click_and_verify_page(context):
    context.driver.wait.until(EC.presence_of_element_located(LINKS), message="Links are not present")
    total_links = context.driver.find_elements(*LINKS)

    item = 0
    while item != len(total_links):
        item += 1
        locator_string = '//div[@class="_p13n-zg-nav-tab-all_style_zg-tabs__EYPLq"]//li[' + f'{item}]'
        context.driver.find_element(By.XPATH, locator_string).click()
        expected_text = context.driver.find_element(By.XPATH, locator_string).text
        sleep(2)

        actual_text = context.driver.find_element(By.ID, 'zg_banner_text').text

        assert expected_text in actual_text, f'{expected_text} Page is not opened'



