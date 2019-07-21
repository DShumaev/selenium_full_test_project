from selenium.webdriver.common.by import By

class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators(object):
    LOGIN_EMAIL_FIELD = (By.CSS_SELECTOR, '#id_login-username')
    LOGIN_PSWD_FIELD = (By.CSS_SELECTOR, '#id_login-password')
    REG_EMAIL_FIELD = (By.CSS_SELECTOR, '#id_registration-email')
    REG_PSWD_FIELD = (By.CSS_SELECTOR, '#id_registration-password1')
    CONFIRM_PSWD_FIELD = (By.CSS_SELECTOR, '#id_registration-password2')
    FORGOTPSWD_LINK = (By.CSS_SELECTOR, 'form#login_form p a')
    LOGIN_BTN = (By.CSS_SELECTOR, 'button.btn.btn-lg.btn-primary[name="login_submit"]')
    REG_BTN = (By.CSS_SELECTOR, 'button.btn.btn-lg.btn-primary[name="registration_submit"]')

