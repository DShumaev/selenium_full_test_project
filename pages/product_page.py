from .locators import ProductPageLocators
from .base_page import BasePage


class ProductPage(BasePage):

    def add_to_cart(self):
        self.should_be_add_to_cart_button()
        self.add_to_cart_click()
        self.solve_quiz_and_get_code()

    def check_product_description_in_notice(self):
        message_name_product = self.get_element_text(*ProductPageLocators.MESSAGE_NAME_PRODUCT)
        name_product = self.get_element_text(*ProductPageLocators.NAME_PRODUCT)        
        if message_name_product == name_product:
            assert True
        else:
            assert False, "Name of added product not match to real name"

    def check_product_price_in_notice(self):
        message_price_product = self.get_element_text(*ProductPageLocators.MESSAGE_PRICE_PRODUCT)
        price_product = self.get_element_text(*ProductPageLocators.PRICE_PRODUCT)
        if message_price_product == price_product:
            assert True
        else:
            assert False, "Name of added product not match to real name"

    def add_to_cart_click(self):
        login_link = self.browser.find_element(*ProductPageLocators.ADDTO_BTN)
        login_link.click()

    def should_be_add_to_cart_button(self):
        assert self.is_element_present(*ProductPageLocators.ADDTO_BTN), \
            "Add to cart button is not present"

    def should_nod_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_SUCCESS), \
            "Success message is presented, but should not be"

    def should_success_message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_SUCCESS), \
            "Success message is not disappeared"

  
