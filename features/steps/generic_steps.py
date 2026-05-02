from behave import given, when, then, step


@given('Store original window')
def store_original_window(context):
    context.original_window = context.app.page.get_current_window()
    print('Original window', context.original_window)


@when('Switch to a new window')
def switch_window(context):
    context.app.page.switch_to_new_window()


@step('Close current page')
def close_page(context):
    context.app.page.close()


@step('Return to original window')
def return_to_original_window(context):
    context.app.page.switch_to_window_by_id(context.original_window)


@when('Refresh the page')
def refresh_page(context):
    context.app.page.refresh_page()