from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators
import math


class BasePage(object):

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, selector_type, selector_value):
        try:
            self.browser.find_element(selector_type, selector_value)
        except (NoSuchElementException):
            return False
        return True

    def get_element_text(self, selector_type, selector_value):
        return self.browser.find_element(selector_type, selector_value).text

    def is_not_element_present(self, selector_type, selector_value, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((selector_type, selector_value)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, selector_type, selector_value, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until_not(EC.presence_of_element_located((selector_type, selector_value)))
        except TimeoutException:
            return False
        return True

    def go_to_login_page(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            print("Your code: {}".format(alert.text))
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def go_to_cart_page(self):
        cart_button = self.browser.find_element(*BasePageLocators.CART_BTN)
        cart_button.click()

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented, probably unauthorised user"

    def fill_the_field(self, selector_type, selector_value, value):
        field = self.browser.find_element(selector_type, selector_value)
        field.send_keys(value)

    def click_element(self, selector_type, selector_value):
        element = self.browser.find_element(selector_type, selector_value)
        element.click()





