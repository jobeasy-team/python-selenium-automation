from behave import given, when, then, step


@step('Store current window')
def store_window(context):
    context.original_window = context.app.page.get_current_window_handle()


@when('Switch to new window')
def switch_to_new_window(context):
    context.app.page.switch_to_new_window()


@step('Close current page')
def close_page(context):
    context.app.page.close()


@step('Return to original window')
def switch_to_original_window(context):
    context.app.page.switch_to_window_by_window_id(context.original_window)
