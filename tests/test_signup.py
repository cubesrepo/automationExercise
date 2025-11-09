import pytest

from pages.signup_page import SignupPage


@pytest.mark.signup
class TestSignup:
    @pytest.fixture
    def signup_page(self, driver, delay):
        return SignupPage(driver, delay)

    @pytest.fixture
    def created_account(self, signup_page):
        current_result_url, current_result_account_created, email, password = signup_page.verify_valid_signup_account_info()
        return email, password

    def test_valid_account_info(self, signup_page):
        current_result_url, current_result_account_created, email, password = signup_page.verify_valid_signup_account_info()

        expected_url = "https://automationexercise.com/account_created"
        expected_result_account_created = "ACCOUNT CREATED!"

        assert current_result_url == expected_url, \
            f"Expected URL to be {expected_url}, but got {current_result_url} instead."

        assert current_result_account_created == expected_result_account_created, \
            f"Expected result to be {expected_result_account_created}, but got {current_result_account_created} instead."

    def test_signup_with_existing_email(self, signup_page):
        current_result_email_exist_message = signup_page.verify_signup_with_existing_email()

        expected_result_email_exist_message = "Email Address already exist!"

        assert current_result_email_exist_message == expected_result_email_exist_message, \
            f"Expected result to be {expected_result_email_exist_message}, but got {current_result_email_exist_message} instead."

    def test_signup_without_email_password(self, signup_page):
        current_result_fill_out_field = signup_page.verify_signup_without_email_password()

        expected_result_fill_out_field = "Please fill out this field."

        assert current_result_fill_out_field == expected_result_fill_out_field, \
            f"Expected result to be {expected_result_fill_out_field}, but got {current_result_fill_out_field} instead."

    def test_valid_login(self, signup_page):
        current_url = signup_page.verify_valid_login()

        expected_url = "https://automationexercise.com/"
        assert current_url == expected_url, \
            f"Expected url to be {expected_url}, but got {current_url} instead."








