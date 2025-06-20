from behave import given, when, then


@given('Open Target App page')
def open_target_app_page(context):
    context.app.target_app_page.open_target_app()


@given('Store original window')
def store_window(context):
    context.original_window = context.app.target_app_page.get_current_window_id()


@when('Click Privacy Policy link')
def click_privacy_link(context):
    context.app.target_app_page.click_privacy_link()


@when('Switch to new window')
def switch_window(context):
    context.app.base_page.switch_to_new_window()


@then('Verify Privacy Policy page opened')
def verify_pp_opened(context):
    context.app.privacy_policy_page.verify_pp_opened()


@then('Close current page')
def close_page(context):
    context.app.base_page.close_window()


@then('Return to original window')
def switch_to_original_window(context):
    context.app.base_page.switch_to_window_by_id(context.original_window)