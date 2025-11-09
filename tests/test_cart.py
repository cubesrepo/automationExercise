import pytest

from pages.cart_page import CartPage


@pytest.mark.cart
class TestCart:
    @pytest.fixture
    def cart_page(self, login_driver, delay):
        return CartPage(login_driver, delay)
    def test_valid_add_to_cart_checkout(self, cart_page):
        cart_product_details, checkout_product_details, current_result_order_placed_message = cart_page.verify_add_to_cart_checkout()
        expected_result_order_placed_message = "ORDER PLACED!"
        for cart_detail, checkout_detail in zip(cart_product_details, checkout_product_details):
            assert cart_detail == checkout_detail, \
                f"Product details mismatched cart:{cart_detail} checkout:{checkout_detail}"
        assert current_result_order_placed_message == expected_result_order_placed_message, \
            f"Expected result to be {expected_result_order_placed_message}, but got {current_result_order_placed_message} instead.c"

    def test_cart_with_empty_product(self, cart_page):
        current_result_cart_empty = cart_page.verify_cart_with_empty_product()
        expected_result_cart_empty = "Cart is empty!"

        assert current_result_cart_empty == expected_result_cart_empty, \
            f"Expected result to be {expected_result_cart_empty}, but got {current_result_cart_empty} instead."
