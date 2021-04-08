from datetime import datetime
import inspect
import os
import pytest

from pytest_bdd import given
from selenium import webdriver
from selenium.webdriver import Firefox
from pages.welcome_page import WelcomePage

# Constants

TRELLO_HOME = 'https://trello.com/pl#'
CURRENT_DIR = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
PARENT_DIR = os.path.dirname(CURRENT_DIR)


# Hooks

def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    print(f'Step failed: {step}')


# Fixtures

@pytest.fixture(autouse=True)
def browser():
    profile = webdriver.FirefoxProfile()
    options = webdriver.FirefoxOptions()
    #options.add_argument('-headless')
    profile.set_preference("browser.privatebrowsing.autostart", True)
    driver = Firefox(firefox_profile = profile, firefox_options=options)
    driver.implicitly_wait(10)
    driver.maximize_window() 
    yield driver
    driver.quit()


# Shared Given Steps

@given('the Tello page is displayed')
def open_trello_home_page(browser):
    browser.get(TRELLO_HOME)
    assert WelcomePage(browser).is_opened()


'''
Method for taking the screenshot and saving in the /screenshots directory. It is called in browser fixture
'''
def take_screenshot(browser, test_name):
    screenshots_dir = PARENT_DIR + '\screenshots'
    now = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
    screenshot_file_path = '{}\{}_{}.png'.format(screenshots_dir, test_name, now)
    browser.save_screenshot(screenshot_file_path)
    return screenshot_file_path

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()
    # set a report attribute for each phase of a call, which can
    # be "setup", "call", "teardown"

    setattr(item, "rep_" + rep.when, rep)

def screenshot(browser, request):
    failed_before = request.session.testsfailed
    yield None
    if request.session.testsfailed != failed_before:
        test_name = request.node.name
        take_screenshot(browser, test_name)

@pytest.fixture()
def users():
    def _users(user):
        return user
    return _users


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call':
        driver = item.funcargs['browser']
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            if pytest_html != None:
                extra.append(pytest_html.extras.image("file:///" + take_screenshot(driver, item.name)))
            else:
                take_screenshot(driver, item.name)
        report.extra = extra