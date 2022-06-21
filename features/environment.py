from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from app.application import Application
from Support.logger import logger, MyListener
from selenium.webdriver.support.events import EventFiringWebDriver


def browser_init(context, test_name):  # test_name parameter added for browserstack

    # Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
    # bs_user = ''
    # bs_pw = ''

    # Allure command:
    # behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/tests/product_page.feature
    # input in terminal


    context.driver = webdriver.Chrome(executable_path="/Users/victorjefferson/Desktop/python-selenium-automation/chromedriver")
    # context.driver = webdriver.Safari()
    # context.driver = webdriver.Firefox(executable_path="./geckodriver")

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, timeout=10)
    context.app = Application(context.driver)

    # HEADLESS MODE ####
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # context.driver = webdriver.Chrome(chrome_options=options, executable_path='')

    ### EventFiringWebDriver - log file ###
    ### for drivers ###
    # context.driver = EventFiringWebDriver(
    #     webdriver.Chrome(executable_path='/Users/victorjefferson/Desktop/python-selenium-automation/chromedriver'),
    #     MyListener())

    # for headless mode ###
    # context.driver = EventFiringWebDriver(webdriver.Chrome(chrome_options = options), MyListener())

    ### for browerstack ###
    # desired_cap = {
    #     'browser': 'Firefox',
    #     'os_version': 'Monterey',
    #     'os': 'OS X',
    #     'name': test_name
    # }


# url = f'http://{bs_user}:{bs_pw}@hub-cloud.browserstack.com/wd/hub'
# context.driver = webdriver.Remote(url, desired_capabilities=desired_cap)

def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    # logger.info(f'Started scenario: {scenario.name}')
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        logger.error(f'Step failed: {step}')
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
