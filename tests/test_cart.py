import pytest

from pages.cart_page import CartPage
from pages.product_page import ProductPage
from tests.base_test import BaseTest

@pytest.mark.order(3)
class TestCart(BaseTest):

    def test_removing_all_products_in_cart(self, driver):
        cartpage = CartPage(driver)
        cartpage.verify_deleting_all_products_in_cart()

    def test_checkout_all_products_in_cart(self, driver):
        cartpage = CartPage(driver)
        productpage = ProductPage(driver)
        productpage.verif_add_to_cart_all_products()
        cartpage.verify_checkout_all_products_in_cart()


