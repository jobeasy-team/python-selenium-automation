from behave import given, when, then


@given('Open Target App page')
def open_target_app_page(context):
    context.app.target_app_page.open_target_app()


@when('Click Privacy Policy link')
def click_pp_link(context):
    context.app.target_app_page.click_pp_link()
    # print('All windows after clicking Privacy link', context.driver.window_handles)
    # print('Current window', context.driver.current_window_handle)


@then('Verify Privacy Policy page opened')
def verify_pp_page_opened(context):
    context.app.privacy_policy_page.verify_pp_page_opened()
