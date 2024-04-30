import pytest

from pages.signup_page import SignupPage
from tests.base_test import BaseTest

@pytest.mark.order(1)
class TestSignupPage(BaseTest):

    def test_signup_page_without_name_and_email(self, driver):
        signuppage = SignupPage(driver)
        signuppage.verify_signup_without_name_and_email()

    def test_signup_page_with_existing_account(self, driver):
        signuppage = SignupPage(driver)
        signuppage.verify_signup_with_existing_account()


    def test_signup_page_with_invalid_email(self, driver):
        signuppage = SignupPage(driver)
        signuppage.verify_signup_with_invalid_email()

    def test_signup_page_with_valid_credentials(self, driver):
        signuppage = SignupPage(driver)
        signuppage.verify_signup_with_valid_credentials()