from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.locators import *
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By


class WelcomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    '''
    Method for login
    '''
    def login(self):
        self.click(self.element(*WelcomePageLocators.LOGIN_BUTTON))
        return True

    '''
    Method  for re open the page
    '''
    def open(self):
        self.driver.get("https://trello.com")
        return self.is_opened()
    
    '''
    Method check is page open
    '''
    def is_opened(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(
            WelcomePageLocators.LOGIN_BUTTON))
        return self.is_element_displayed(*WelcomePageLocators.LOGIN_BUTTON)