from .locators import CartPageLocators
from .base_page import BasePage


class CartPage(BasePage):

    def cart_is_empty(self):
        assert self.is_not_element_present(*CartPageLocators.PRODUCT_OBJECT_IN_CART), \
            "The cart is not empty"

    def text_that_cart_is_empty_present(self):
        assert self.is_element_present(*CartPageLocators.STRING_CART_EMPTY), \
            "The text 'cart is empty' is not present"
        assert self.get_element_text(*CartPageLocators.STRING_CART_EMPTY).startswith("Your basket is empty."), \
            "Presented incorrect text in element the cart is empty"
