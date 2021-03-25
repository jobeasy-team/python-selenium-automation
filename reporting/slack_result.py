import os
from json import load
from requests import post

# SLACK_HOOK_URL = 'https://hooks.slack.com/services/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'


def get_automation_name() -> str:
    """
    Gets name of automation job
    :return: environment variable: AUTOMATION_NAME
    """
    return os.environ['AUTOMATION_NAME']


def main():
    automation_space = get_automation_name()  # will use for Jenkins url generation

    # Get stats info
    # open Allure report, statistics widget summary
    print(os.getcwd())
    with open('allure-report/widgets/summary.json') as data_file:
        stats = load(data_file)['statistic']

    total, passed = stats['total'], stats['passed']
    failed = stats['failed'] + stats['broken']
    pass_rate = '{:.2f}'.format(passed / total * 100)

    # Get device info
    # open Allure report, environment widget, find Device line and add to the report
    device_line, platform = '', ''
    with open('allure-report/widgets/environment.json') as data_file:
        environment_info = load(data_file)

    for item in environment_info:
        if item['name'] == 'Device':
            device_line = item['values'][0]
        elif item['name'] == 'Platform':
            platform = item['values'][0]

    # Create Slack message with main stats and device info:
    message = {
        "attachments": [
            {"title": "LoC UI Automation Report: {}".format(platform),
             "text": "https://stage2.meettally.com/jenkins-qa/job/{}\n"
                     "Test Cases total: *{}*\n"
                     "Success Rate: *{}%*\n"
                     "_Passed:_ {}\n"
                     "_Failed:_ {}\n"
                     "_{}_\n".format(
                 automation_space,
                 total,
                 pass_rate,
                 passed,
                 failed,
                 device_line)
             }
        ]
    }
    # Send a Slack message
    post(url=SLACK_HOOK_URL, json=message)


if __name__ == '__main__':
    main()
