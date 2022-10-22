from behave import given, then


@given('Open Amazon Bestsellers')
def open_amazon_bestsellers(context):
    context.app.bestsellers_page.open_bestsellers()


@then('User can click through top links and verify correct page opens')
def click_thru_top(context):
    context.app.bestsellers_page.click_thru_top_links()
