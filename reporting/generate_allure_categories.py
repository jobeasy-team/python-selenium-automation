import json
from support.logger import logger


def generate_allure_categories_file():
    """
    Generates categories.json file, which adds customized categories for Allure report
    """
    data = [{"name": "Crashes!", "messageRegex": ".*crashed.*", "matchedStatuses": ["broken", "failed"]},
            {"name": "Stuck on Sign In screen", "messageRegex": ".*too long for SignIn.*", "matchedStatuses":
                ["broken", "failed"]},
            {"name": "Stuck on Passcode screen", "messageRegex": ".*too long for Passcode.*", "matchedStatuses":
                ["broken", "failed"]},
            {"name": "Stuck on Nice Work screen", "messageRegex": ".*too long for NiceWork.*", "matchedStatuses":
                ["broken", "failed"]},
            {"name": "Back-end Aggregation Error", "messageRegex": ".*AGGREGATION_ERROR.*", "matchedStatuses":
                ["broken", "failed"]},
            {"name": "Back-end Loan Offer Error", "messageRegex": ".*loan_offer.*", "matchedStatuses":
                ["broken", "failed"]},
            {"name": "BrowserStack Device Error", "messageRegex": ".*HT79W1A02662.*", "matchedStatuses":
                ["broken", "failed"]}
            ]
    try:
        with open('allure-results/categories.json', 'w') as outfile:
            json.dump(data, outfile)
    except Exception as e:
        logger.warn(e)
