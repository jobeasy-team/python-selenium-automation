import logging
from selenium.webdriver.support.events import AbstractEventListener

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

handler = logging.FileHandler('./mobile_automation.log')
handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


def clean_log_file(file='mobile_automation.log'):
    open(file, 'w').close()


def log_scenario_name(name):
    logger.info('=' * 73)
    logger.info("Scenario: {}".format(name))
    logger.info('=' * 73)


class MyListener(AbstractEventListener):
    logger = logger

    def before_find(self, by, value, driver):
        message = "Searching element by {} => '{}' ".format(by, value)
        logger.info(message)

    def after_find(self, by, value, driver):
        message = "Found the element by {} => '{}' ".format(by, value)
        logger.info(message)

    def on_exception(self, exception, driver):
        logger.warning(exception)
