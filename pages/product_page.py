from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from .base_page import BasePage

class ProductPage(BasePage):

    def add_to_basket(self):
        basket_button = self.browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
        basket_button.click()

    def should_be_added_to_basket_message(self):
        assert self.is_element_present(By.CSS_SELECTOR, "#messages > div:nth-child(1) > div"), "No added to basket message"

    def should_be_correct_price_message(self):
        assert self.is_element_present(By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong"), "No correct price message"

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True