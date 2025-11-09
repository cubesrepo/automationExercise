import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utilities import test_data


class CartPage(BasePage):
    def click_products_menu(self):
        self.action_click(test_data.homepage.PRODUCTS_MENU)
    def click_cart_menu(self):
        self.wait_clickable(test_data.homepage.CART_MENU).click()
    def click_continue_shopping(self):
        self.wait_clickable(test_data.products.CONTINUE_SHOPPING).click()
    def click_proceed_to_checkout(self):
        self.wait_clickable(test_data.cart.PROCEED_CHECKOUT_BTN).click()
    def click_place_order(self):
        self.wait_clickable(test_data.cart.PLACE_ORDER).click()

    def get_product_name(self):
        product_name = []
        for i in range(6):
            locator = By.CSS_SELECTOR, f"a[href='/product_details/{i}']"
            text = self.get_text(locator)
            product_name.append(text)
        return product_name

    def hover_product(self, index):
        hover_locator = By.XPATH, f"(//div[@class='productinfo text-center'])[{index}]"
        self.hover(hover_locator)

    def add_to_cart_products(self):
        index = 1
        for i in range(2, 11, 2):
            element = By.XPATH, f"(//a[contains(text(),'Add to cart')])[{i}]"
            self.hover_product(index)
            self.wait_clickable(element).click()
            self.click_continue_shopping()
            index += 1
    def add_payment(self, card_name, card_number, cvc, month, year):
        payment_info = {
            test_data.cart.NAME_ON_CARD: card_name,
            test_data.cart.CARD_NUMBER: card_number,
            test_data.cart.CVC: cvc,
            test_data.cart.MONTH: month,
            test_data.cart.YEAR: year
        }
        for locator, value in payment_info.items():
            self.type(locator, value)
    def click_confirm_order(self):
        element = self.wait_clickable(test_data.cart.PAY_AND_CONFIRM_ORDER)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        element.click()

    def remove_product(self):
        for i in range(1, 6):
            locator = By.XPATH, f"(//a[@class='cart_quantity_delete'])[{i}]"
            element = self.wait_clickable(locator)
            element.click()

    def verify_add_to_cart_checkout(self):
        self.click_products_menu()
        self.add_to_cart_products()
        self.click_cart_menu()
        current_result_cart_product_details = self.get_product_name()
        self.click_proceed_to_checkout()
        current_result_checkout_product_details = self.get_product_name()
        self.click_place_order()
        self.add_payment("Testcard", "55123", "311",
                         "05", "2029")
        self.click_confirm_order()
        current_result_order_placed_message = self.get_text(test_data.cart.ORDER_PLACE_MESSAGE)

        return current_result_cart_product_details, current_result_checkout_product_details, current_result_order_placed_message

    def verify_cart_with_empty_product(self):
        self.click_products_menu()
        self.add_to_cart_products()
        self.click_cart_menu()
        self.remove_product()

        current_result_cart_empty = self.get_text(test_data.cart.CART_EMPTY_MESSAGE)

        return current_result_cart_empty
