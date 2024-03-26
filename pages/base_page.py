import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def __init__(self, browser, url, timeout=10):
    self.browser = browser
    self.url = url
    self.browser.implicitly_wait(timeout)


class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)
