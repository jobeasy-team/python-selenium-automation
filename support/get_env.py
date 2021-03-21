import os


def get_bs_user():
    if 'BS_USER' in os.environ:
        return os.environ['BS_USER']
    else:
        raise ValueError('No BrowserStack USERNAME provided')


def get_bs_key():
    if 'BS_KEY' in os.environ:
        return os.environ['BS_KEY']
    else:
        raise ValueError('No BrowserStack KEY provided')
