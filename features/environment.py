from selenium import webdriver
from selenium.webdriver.support.events import EventFiringWebDriver


from app.application import Application
from support.get_env import get_bs_key, get_bs_user
from support.logger import logger, MyListener


def browser_init(context, test_name):
    """
    :param context: Behave context
    """
    browserstack_url = f'http://{get_bs_user()}:{get_bs_key()}@hub-cloud.browserstack.com/wd/hub'
    desired_cap = {
        'browser': 'Chrome',
        'browser_version': '87',
        'name': test_name
    }
    remote_driver = webdriver.Remote(command_executor=browserstack_url, desired_capabilities=desired_cap)
    context.driver = EventFiringWebDriver(remote_driver, MyListener())
    # context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.implicitly_wait(5)
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name)


def before_step(context, step):
    logger.info(f'Step: {step.name}')


def after_step(context, step):
    if step.status == 'failed':
        logger.error(f"Step FAILED: '{step.name}'")


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
