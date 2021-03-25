from allure import attach
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.support.events import EventFiringWebDriver

from app.application import Application
from reporting.browserstack_api import BSSession
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
    # context.driver = EventFiringWebDriver(webdriver.Chrome(), MyListener())
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
        # Attach a screenshot to Allure report in case the step fails
        attach(
            context.driver.get_screenshot_as_png(),
            name=f'{step.name}.png',
            attachment_type=AttachmentType.PNG
        )


def after_scenario(context, feature):
    bs_session = BSSession(get_bs_user(), get_bs_key(), context.driver.session_id)
    bs_link = bs_session.get_browser_url()
    #  If run via BS, attach link to a remote BS session to the report
    attach(bs_link, name='BrowserStack Session', attachment_type=AttachmentType.URI_LIST)

    context.driver.delete_all_cookies()
    context.driver.quit()
    logger.info('Scenario finished.\n\n')
