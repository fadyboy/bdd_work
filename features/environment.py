# environment file for BDD tests

import logging
from selenium import webdriver


# code to execute before any test is run
def before_all(context):
    selenium_logger = logging.getLogger('selenium.webdriver.remote.remote_connection')
    selenium_logger.setLevel(logging.WARN)
    context.browser = webdriver.Firefox()

# code to execute after any test is run
def after_all(context):
    context.browser.quit()
