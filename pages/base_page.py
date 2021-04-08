from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium import webdriver
from pages.locators import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    '''
    Method which convert the locator to web element
    '''
    def element(self, *locator):
        WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)
    '''
    Method which convert the locator to web elements list
    '''
    def elements(self, *locator):
        return self.driver.find_elements(*locator)
    
    '''
    Method which input the text to text fields
    '''
    def type(self, element, value):
        # ADD HERE WAIT UNTIL THE BUTTON IS CLIKACBLE
        clickable = False
        while clickable is False:
            element.clear()
            element.send_keys(value)
            element.click()
            clickable = bool(len(element.get_attribute('value')) == len(value))
            print("-----------------------------------")
            print(value)
            print(clickable)
        return clickable
        
    '''
    Method clicks on the element
    '''
    def click(self, element):
        WebDriverWait(self.driver, 1).until(
            EC.invisibility_of_element_located((By.CLASS_NAME, "modal fade ng-isolate-scope ng-animate ng-leave ng-leave-active")))
        element.click()
        return True

    
    '''
    Method which gets the placeholder value of text field
    '''
    def get_input_value(self, element):
        if element is not None:
            while element.get_attribute("value") == "":
               continue
            return element.get_attribute("value")
    
    '''
    Method which gets the placeholder value of text field if empty
    '''
    def get_input_empty_value(self, element):
        if element is not None:
            while element.get_attribute("value") != "":
               continue
            return element.get_attribute("value")
    '''
    Method which checks the placeholder value of text field
    '''
    def check_input_value(self, element = None, user_field = None):
        if user_field is not None:
            if user_field == "":
                return self.get_input_empty_value(element) == str(user_field)
            else:
                return self.get_input_value(element) == str(user_field)
        elif user_field is None:
            return self.get_input_value(element) == ""

    
    '''
    Method which check if element is displayed or not
    '''
    def is_element_displayed(self, *locator):
        try: 
            if self.driver.find_element(*locator).is_displayed():
                return True
        except:
            return False