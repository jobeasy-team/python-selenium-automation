from behave import given, when, then


@given('Open main target page')
def open_target_main(context):
    context.app.main_page.open_main()
