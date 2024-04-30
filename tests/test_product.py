import pytest

from pages.product_page import ProductPage
from tests.base_test import BaseTest

@pytest.mark.order(2)
class TestProductPage(BaseTest):


    def test_add_to_cart_all_products(self, driver):
        productpage = ProductPage(driver)
        productpage.verif_add_to_cart_all_products()