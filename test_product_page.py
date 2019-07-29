from .pages.product_page import ProductPage
from .pages.cart_page import CartPage
import pytest


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"

#@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_cart(browser):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_cart()
    product_page.check_product_description_in_notice()
    product_page.check_product_price_in_notice()

def test_guest_cant_see_success_message(browser):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_nod_be_success_message()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.go_to_login_page()

def test_guest_cant_see_product_in_cart_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    product_page = ProductPage(browser, link)
    product_page.open()
    print("open start page")
    product_page.go_to_cart_page()
    print("open cart page")
    cart_page = CartPage(browser, browser.current_url)
    print("load cartpage object")
    cart_page.text_that_cart_is_empty_present()
    cart_page.cart_is_empty()
    

