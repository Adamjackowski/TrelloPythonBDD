"""
This module contains step definitions for web.feature.
It uses Selenium WebDriver for browser interactions:
https://www.seleniumhq.org/projects/webdriver/
Setup and cleanup are handled using hooks.
For a real test automation project,
use Page Object Model or Screenplay Pattern to model web interactions.

Prerequisites:
 - Firefox must be installed.
 - geckodriver must be installed and accessible on the system path.
"""

import distutils
from pages.objects.user import User
from tests.step_defs.conftest import users
from pages.login_page import LoginPage
from pages.welcome_page import WelcomePage
from pytest_bdd import scenario, scenarios, when, then, parsers
from pytest_bdd.steps import given
from selenium.webdriver.common.keys import Keys
from distutils import util

# Constants

TRELLO_HOME = 'https://trello.com/pl#'


# Scenarios

#scenarios('../features/trello.feature')
@scenario(
    '../features/trello.feature',
    'Login with wrong credentials',
    example_converters=dict(login=str, password=str, attasian=bool)
)

def test_trello():
    pass

# When Steps

@when(parsers.parse('the user wants to login with <attlasian> <login> login and <password> password'))
def login(browser, login, password, attlasian, users):
    assert WelcomePage(browser).login()
    login_page = LoginPage(browser)
    assert login_page.is_opened()
    assert login_page.login(users(User(email=login, password=password)), attlasian=bool(distutils.util.strtobool(attlasian)))

# Then Steps

@then(parsers.parse('login fails'))
def login_fails(browser):
    assert LoginPage(browser).is_login_failed()
    assert WelcomePage(browser).open()
