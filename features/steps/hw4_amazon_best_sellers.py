from selenium.webdriver.common.by import By
from behave import given, then


@given('Open Amazon bestSeller page')
def open_amazon(context):
    # open the url
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')


@then('bestseller page is shown')
def best_seller_shown(context):
    result_obj = context.driver.find_element(By.CSS_SELECTOR, "#zg_banner_text")
    assert result_obj.text == "Amazon Best Sellers", f"Error, didn't open best sellers page, but {result_obj.text} page"


@then('{number_links} links display on the page')
def links_display(context, number_links):
    link_array = context.driver.find_elements(By.CSS_SELECTOR, "._p13n-zg-nav-tab-all_style_zg-tabs__EYPLq li")
    assert len(link_array) == int(number_links), f"Error, number of links is not {number_links}, but {len(link_array)}"
    print('Test Passed')
