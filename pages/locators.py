from selenium.webdriver.common.by import By


class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')

class LoginPageLocators(object):

    LOGIN_PSWD_FIELD = (By.CSS_SELECTOR, '#id_login-password')
    REG_EMAIL_FIELD = (By.CSS_SELECTOR, '#id_registration-email')
    REG_PSWD_FIELD = (By.CSS_SELECTOR, '#id_registration-password1')
    CONFIRM_PSWD_FIELD = (By.CSS_SELECTOR, '#id_registration-password2')
    FORGOTPSWD_LINK = (By.CSS_SELECTOR, 'form#login_form p a')
    LOGIN_BTN = (By.CSS_SELECTOR, 'button.btn.btn-lg.btn-primary[name="login_submit"]')
    REG_BTN = (By.CSS_SELECTOR, 'button.btn.btn-lg.btn-primary[name="registration_submit"]')

class ProductPageLocators(object):
    NOTICE_NAME_PRODUCT = (By.CSS_SELECTOR, 'div#messages>div:nth-child(1)>div.alertinner>strong')
    NOTICE_STATUS_BASKET = (By.CSS_SELECTOR, 'div#messages>div:nth-child(2)>div.alertinner>strong')
    NOTICE_PRICE_PRODUCT = (By.CSS_SELECTOR, 'div#messages>div:nth-child(3)>div.alertinner strong')
    NAME_PRODUCT = (By.CSS_SELECTOR, 'div.row>div>h1')
    PRICE_PRODUCT = (By.CSS_SELECTOR, 'div.row>div>p.price_color')
    ADDTO_BTN = (By.CSS_SELECTOR, 'button.btn-add-to-basket')



