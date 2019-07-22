from .locators import ProductPageLocators
from .base_page import BasePage


class ProductPage(BasePage):

    def add_to_cart(self):
        self.should_be_add_to_basket_button()
        self.go_to_basket_page()
        self.solve_quiz_and_get_code()

    def check_product_description_in_notice(self):
        notice_name_product = self.get_element_text(*ProductPageLocators.NOTICE_NAME_PRODUCT)
        name_product = self.get_element_text(*ProductPageLocators.NAME_PRODUCT)        
        if notice_name_product == name_product:
            assert True
        else:
            assert False, "Name of added product not match to real name"

    def check_product_price_in_notice(self):
        notice_price_product = self.get_element_text(*ProductPageLocators.NOTICE_PRICE_PRODUCT)
        price_product = self.get_element_text(*ProductPageLocators.PRICE_PRODUCT)
        if notice_price_product == price_product:
            assert True
        else:
            assert False, "Name of added product not match to real name"

    def go_to_basket_page(self):
        login_link = self.browser.find_element(*ProductPageLocators.ADDTO_BTN)
        login_link.click()

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADDTO_BTN), "Add to basket button is not present"

   
