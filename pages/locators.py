from selenium.webdriver.common.by import By

class WelcomePageLocators(object):
   LOGIN_BUTTON = (By.CSS_SELECTOR, ".btn-link")

class LoginPageLocators(object):
   EMAIL_INPUT = (By.ID, "user")
   PASSWORD_INPUT = (By.ID, "password")
   LOGIN_BUTTON = (By.ID, "login")
   ERROR_MESSAGE = (By.CSS_SELECTOR, "p.error-message")
   LOGIN_BUTTON_ATTLASIAN = (By.ID, "login-submit")