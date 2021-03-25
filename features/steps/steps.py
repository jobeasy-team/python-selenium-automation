from behave import given, when, then


@given('Open main page')
def open_wiki_main_page(context):
    context.app.main_page.open_page()


@when('Search for {query}')
def search(context, query):
    context.app.right_navigation.search(query)


@when('Click to create article')
def create_article(context):
    context.app.no_search_results_page.click_create_page()


@then('Verify correct UI elements are shown on main page')
def verify_ui_elements(context):
    context.app.main_page.verify_ui_elements()


@then('Verify article opens for {query}')
def verify_article_opens(context, query):
    context.app.article_page.verify_article_header(query)


@then('Verify No Search Results page opens')
def verify_no_results_opens(context):
    context.app.no_search_results_page.verify_page_opened()

