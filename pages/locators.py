from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    def user_login(self):
        email_address = (By.NAME, "login-username")

    def user_registration(self):
        email = (By.NAME, "registration-email")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

