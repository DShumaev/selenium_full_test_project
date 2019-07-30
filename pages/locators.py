from selenium.webdriver.common.by import By

class BasePageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#login_link_inc')
    CART_BTN = (By.CSS_SELECTOR, 'span.btn-group>a.btn.btn-default')
    USER_ICON = (By.CSS_SELECTOR, '.icon-user')

class LoginPageLocators(object):
    LOGIN_EMAIL_FIELD = (By.CSS_SELECTOR, '#id_login-username')
    LOGIN_PSWD_FIELD = (By.CSS_SELECTOR, '#id_login-password')
    REG_EMAIL_FIELD = (By.CSS_SELECTOR, '#id_registration-email')
    REG_PSWD_FIELD = (By.CSS_SELECTOR, '#id_registration-password1')
    CONFIRM_PSWD_FIELD = (By.CSS_SELECTOR, '#id_registration-password2')
    FORGOTPSWD_LINK = (By.CSS_SELECTOR, 'form#login_form p a')
    LOGIN_BTN = (By.CSS_SELECTOR, 'button.btn.btn-lg.btn-primary[name="login_submit"]')
    REG_BTN = (By.CSS_SELECTOR, 'button.btn.btn-lg.btn-primary[name="registration_submit"]')

class ProductPageLocators(object):
    MESSAGE_NAME_PRODUCT = (By.CSS_SELECTOR, 'div#messages>div:nth-child(1)>div.alertinner>strong')
    MESSAGE_STATUS_BASKET = (By.CSS_SELECTOR, 'div#messages>div:nth-child(2)>div.alertinner>strong')
    MESSAGE_PRICE_PRODUCT = (By.CSS_SELECTOR, 'div#messages>div:nth-child(3)>div.alertinner strong')
    NAME_PRODUCT = (By.CSS_SELECTOR, 'div.row>div>h1')
    PRICE_PRODUCT = (By.CSS_SELECTOR, 'div.row>div>p.price_color')
    ADDTO_BTN = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    MESSAGE_SUCCESS = (By.CSS_SELECTOR, 'div#messages>div.alert-success:nth-child(1)')

class CartPageLocators(object):
    MESSAGE_CART_EMPTY = (By.CSS_SELECTOR, 'div#messages>div.alert-info div.alertinner>p')
    PRODUCT_OBJECT_IN_CART = (By.CSS_SELECTOR, 'div.basket-items')
    STRING_CART_EMPTY = (By.CSS_SELECTOR, 'div#content_inner>p')





