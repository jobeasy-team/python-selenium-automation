from behave import given, when, then


@given('Open Help page for Returns')
def click_cart(context):
    context.app.help_page.open_help_returns()


@when('Select Help topic {topic}')
def select_topic(context, topic):
    context.app.help_page.select_topic(topic)


@then('Verify help {expected_text} page opened')
def verify_header_present(context, expected_text):
    context.app.help_page.verify_header_present(expected_text)


# @then('Verify help Current promotions page opened')
# def verify_promotions_opened(context):
#     context.app.help_page.verify_promotions_opened()
#
#
# @then('Verify help Returns page opened')
# def verify_returns_opened(context):
#     context.app.help_page.verify_returns_opened()
#
#
# @then('Verify help About Target Circle page opened')
# def verify_about_target_circle_opened(context):
#     context.app.help_page.verify_about_target_circle_opened()