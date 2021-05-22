import os


class Configuration:
    subdomain = os.environ.get('SUBDOMAIN')
    email = os.environ.get('EMAIL_ADDRESS')
    password = os.environ.get('PASSWORD')
