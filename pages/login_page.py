from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.locators import LoginPageLocators

class LoginPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)
    '''
    Method check is page open
    '''
    def is_opened(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(
            LoginPageLocators.LOGIN_BUTTON))
        return self.is_element_displayed(*LoginPageLocators.LOGIN_BUTTON)

    '''
    Method for login in.
    '''
    def login(self, user, attlasian=True):
        self.fill_fields(user, attlasian)
        if attlasian is True:
            self.click(self.element(*LoginPageLocators.LOGIN_BUTTON_ATTLASIAN))
        else:
            self.click(self.element(*LoginPageLocators.LOGIN_BUTTON))
        return True

    '''
    Method for filling in fields
    '''
    def fill_fields(self, user, attlasian):
        self.type(self.element(*LoginPageLocators.EMAIL_INPUT), user._email)
        self.click(self.element(*LoginPageLocators.LOGIN_BUTTON))
        if attlasian is True:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(LoginPageLocators.LOGIN_BUTTON_ATTLASIAN))
        self.type(self.element(*LoginPageLocators.PASSWORD_INPUT), user._password)
    
    '''
    Method checks filled fields
    '''
    def check_filled_fields(self, user):
        assert self.check_input_value(self.element(*LoginPageLocators.EMAIL_INPUT), user._email)
        assert self.check_input_value(self.element(*LoginPageLocators.PASSWORD_INPUT), user._password)

    '''
    Method checks if error message is displayed
    '''
    def is_error_message(self):
        WebDriverWait(self.driver, 5).until(
        EC.visibility_of_element_located(LoginPageLocators.ERROR_MESSAGE))
        self.is_element_displayed(*LoginPageLocators.ERROR_MESSAGE)
        return True
        
    '''
    Method checks if the login is failed
    '''
    def is_login_failed(self):
        assert self.is_opened()
        assert self.is_error_message()
        return True

    