from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        login_link = self.browser.current_url.find("login")
        if login_link == -1:
            assert False, "This url does not match the login page"
        else:
            assert True

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL_FIELD), "Email adress field is not presented on the login page"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PSWD_FIELD), "Password field is not presented on the login page"
        assert self.is_element_present(*LoginPageLocators.FORGOTPSWD_LINK), "Restore password link is not presented on the login page"
        assert self.is_element_present(*LoginPageLocators.LOGIN_BTN), "Login button is not presented on the login page"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_EMAIL_FIELD), "Email adress field is not presented on the login page"
        assert self.is_element_present(*LoginPageLocators.REG_PSWD_FIELD), "Password field is not presented on the login page"
        assert self.is_element_present(*LoginPageLocators.CONFIRM_PSWD_FIELD), "Password confirm field is not presented on the login page"
        assert self.is_element_present(*LoginPageLocators.REG_BTN), "Register button is not presented on the login page"
