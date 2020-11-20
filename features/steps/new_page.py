from behave import given, then
from selenium.webdriver.common.by import By


#TOP_LINKS = (By.CSS_SELECTOR, "a[href*='ref=zg_bs_tab']")
TOP_LINKS = (By.CSS_SELECTOR, "#zg_tabs a")
VERIFY_MESSAGE =(By.CSS_SELECTOR, "#zg_banner_text_wrapper")

@given("Open amazon Bestsellers page")
def open_bestsellers(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')



@then("Clicks on each top link and verify that new page opens")
def click_top(context):
    top_links = context.driver.find_elements(*TOP_LINKS)

    for x in range(len(top_links)):
        top_links = context.driver.find_elements(*TOP_LINKS)
        link = top_links[x]
        link_text = link.text
        link.click()
        verify_text = context.driver.find_element(*VERIFY_MESSAGE).text
        assert link_text in verify_text, f"Expected {link_text} not in {VERIFY_MESSAGE}"