from selenium import webdriver
from app.application import Application
from selenium.webdriver.support.wait import WebDriverWait


def browser_init(context):
    """
    :param context: Behave context
    """
    context.driver = webdriver.Chrome(executable_path='C:\\Users\\Adewale\\OneDrive\\Desktop\\Automation Course\\python-selenium-automation\\chromedriver.exe')
    # context.browser = webdriver.Safari()
    # context.browser = webdriver.Firefox()

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.app = Application(context.driver)



def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
