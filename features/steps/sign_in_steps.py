from behave import then


@then('Verify Sign in page opened')
def verify_sign_in_opened(context):
    context.app.sign_in_page.verify_signin_opened()