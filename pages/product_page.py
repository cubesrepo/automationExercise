import time

from selenium.webdriver.common.by import By

import test_data
from pages.base_page import BasePage
from selenium.common import ElementClickInterceptedException

class ProductPage(BasePage):

    def verif_add_to_cart_all_products(self):
        time.sleep(2)

        #click product menu
        self.wait_clickable(test_data.homepage.PRODUCTS_MENU, 15).click()
        time.sleep(1)

        #assert page title and url
        assert self.url_is("https://automationexercise.com/products")
        assert self.title_is("Automation Exercise - All Products")

        time.sleep(0.5)

        index = 0
        for prod in range(1, 35):
            product_item = By.XPATH, f"(//div[@class='productinfo text-center'])[{prod}]"
            product = self.wait_presence(product_item,15)
            self.action_move_to_element(product)
            time.sleep(0.5)

            index += 2
            #CLICK ADD TO CART ITEM
            add_to_cart_item = By.XPATH, f"(//a[@class='btn btn-default add-to-cart'][normalize-space()='Add to cart'])[{index}]"
            try:
                self.wait_clickable(add_to_cart_item, 15).click()
            except ElementClickInterceptedException:
                self.action_click(add_to_cart_item)

            time.sleep(0.5)

            #CLICK CONTINUE SHOPPING
            self.wait_clickable(test_data.products.CONTINUE_SHOPPING, 15).click()
            time.sleep(0.5)