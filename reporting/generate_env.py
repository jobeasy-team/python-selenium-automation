from support.logger import logger


def generate_env(capabilities, env):
    """
    Generates environment.properties file for Allure report
    """
    try:
        env_f = open('allure-results/environment.properties', 'w')
        env_f.write(
            f"Environment: {env.capitalize()}\n"
            f"Platform: {capabilities['os']}\n"
            f"Device: {capabilities['device']}, {capabilities['os_version']}\n"
            f"URL_App: {capabilities['app']}\n"
        )
        env_f.close()
    except Exception as e:
        logger.warn(e)
