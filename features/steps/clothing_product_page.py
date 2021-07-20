from selenium.webdriver.common.by import By
from behave import given, when, then

@given('Open Amazon clothing page')
def open_cloth_page(context):
    context.app.clothing_page.open_cloth_page()