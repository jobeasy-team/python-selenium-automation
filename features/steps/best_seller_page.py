from selenium.webdriver.common.by import By
from time import sleep
from behave import then

HEADER_LINKS = (By.XPATH, "//div[@id = 'zg_tabs']//ul//li//a")
BANNER_TEXT = (By.CSS_SELECTOR, "div#zg_banner_text_wrapper")


@then("User can navigate through the header menu links "
      "and verify banner is matching link text")
def navigate_through_header_links(context):

    header_menu_links = context.driver.find_elements(*HEADER_LINKS)

    for link in range(len(header_menu_links)):

        current_link_click = context.driver.find_elements(*HEADER_LINKS)[link]
        link_text = current_link_click.text
        current_link_click.click()
        sleep(1)

        banner_text = context.driver.find_element(*BANNER_TEXT).text
        assert link_text in banner_text, f"Expected {link_text} in {banner_text}"

