import random
import string
import time

import test_data
from pages.base_page import BasePage


class CartPage(BasePage):

    def verify_deleting_all_products_in_cart(self):
        time.sleep(2)

        #click cart menu
        self.wait_clickable(test_data.homepage.CART_MENU, 15).click()

        time.sleep(1)

        assert self.url_is("https://automationexercise.com/view_cart")

        while True:
            try:
                delete_btn = self.wait_clickable(test_data.cart.DELETE, 5)
            except:
                break

            if delete_btn:
                self.action_click(delete_btn)
                time.sleep(0.5)
            else:
                break
        assert self.wait_visibility(test_data.cart.CART_EMPTY_MESSAGE,15)

    def verify_checkout_all_products_in_cart(self):
        time.sleep(2)
        # click cart menu
        self.wait_clickable(test_data.homepage.CART_MENU, 15).click()
        time.sleep(0.5)
        #click proceed checkout
        self.wait_clickable(test_data.cart.PROCEED_CHECKOUT_BTN, 15).click()

        time.sleep(1)

        #check page title and url
        assert self.url_is("https://automationexercise.com/checkout")
        assert self.title_is("Automation Exercise - Checkout")

        #input comments
        commentvalue = "like to order all products"
        self.send_keys(15, test_data.cart.COMMENT, commentvalue)

        time.sleep(0.5)

        #click place order
        self.wait_clickable(test_data.cart.PLACE_ORDER,15).click()

        time.sleep(1)

        #input name on card
        namevalue = ''.join(random.choices(string.ascii_lowercase, k=7))
        self.send_keys(15, test_data.cart.NAME_ON_CARD, namevalue)

        time.sleep(0.5)

        # input card number
        cardnumbervalue = ''.join(random.choices(string.digits, k=7))
        self.send_keys(15, test_data.cart.CARD_NUMBER, cardnumbervalue)

        time.sleep(0.5)

        # input cvc
        cvcvalue = ''.join(random.choices(string.digits, k=4))
        self.send_keys(15, test_data.cart.CVC, cvcvalue)

        time.sleep(0.5)

        # input month
        monthvalue = "12"
        self.send_keys(15, test_data.cart.MONTH, monthvalue)

        time.sleep(0.5)

        # input year
        yearvalue = "2028"
        self.send_keys(15, test_data.cart.YEAR, yearvalue)

        time.sleep(0.5)

        #click submit
        self.wait_clickable(test_data.cart.SUBMIT, 15).click()

        time.sleep(1)

        #assert if the order place message is display
        assert self.wait_visibility(test_data.cart.ORDER_PLACE_MESSAGE, 15)