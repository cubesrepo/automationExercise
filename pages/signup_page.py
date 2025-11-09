from allure_commons.model2 import TEST_CASE_PATTERN
from faker.proxy import Faker

from pages.base_page import BasePage
from tests.test_cart import TestCart
from utilities import test_data


class SignupPage(BasePage):
    def click_signup_login_menu(self):
        self.wait_clickable(test_data.homepage.SIGNUP_LOGIN_MENU).click()

    def type_name_email_signup(self, name, email):
        self.type(test_data.signup.NAME, name)
        self.type(test_data.signup.EMAIL_ADDRESS, email)

    def type_email_password_login(self, email, password):
        self.type(test_data.login.EMAIL, email)
        self.type(test_data.login.PASSWORD, password)

    def click_signup_btn(self):
        self.wait_clickable(test_data.signup.SIGNUP_BTN).click()

    def set_title(self, title):
        if title.lower().strip() == "mr":
            self.wait_clickable(test_data.signup.MR).click()
        elif title.lower().strip() == "mrs":
            self.wait_clickable(test_data.signup.MRS).click()

    def enter_password(self, password):
        self.scroll_to_element(test_data.signup.PASSWORD)
        return self.type( test_data.signup.PASSWORD, password)

    def enter_date_of_birth(self, day, month, year):
        self.select_dropdown_value(test_data.signup.DAY, day)
        self.select_dropdown_value(test_data.signup.MONTH, month)
        self.select_dropdown_value(test_data.signup.YEAR, year)

    def set_country(self, country):
        self.select_dropdown_value(test_data.signup.COUNTRY, country)
    def tick_newsletter_special_offer(self):
        self.wait_clickable(test_data.signup.NEWS_LETTER).click()
        self.wait_clickable(test_data.signup.SPECIAL_OFFER).click()

    def enter_address_information(self, first_name, last_name, company, address, address_2, country,
                                  state, city, zip_code, mobile_number):
        print(f"pipi {first_name}")
        address_info = {
            test_data.signup.FIRST_NAME: first_name,
            test_data.signup.LAST_NAME: last_name,
            test_data.signup.COMPANY: company,
            test_data.signup.ADDRESS_ONE: address,
            test_data.signup.ADDRESS_TWO: address_2,
            test_data.signup.STATE: state,
            test_data.signup.CITY: city,
            test_data.signup.ZIP_CODE: zip_code,
            test_data.signup.MOBILE_NO: mobile_number
        }

        for locator, value in address_info.items():
            self.scroll_to_element(locator)


            if value in "STATE":
                self.set_country(country)
            self.type(locator, value)



    def click_create_account(self):
        self.wait_clickable(test_data.signup.CREATE_ACCOUNT_BTN).click()

    def get_account_created_url(self, url):
        return self.get_url(url)
    def get_account_created_message(self):
        return self.get_text(test_data.signup.ACCOUNT_CREATED_MESSAGE)
    def get_email_exist_message(self):
        return self.get_text(test_data.signup.EMAIL_ALREADY_EXIST_MESSAGE)
    def click_login_btn(self):
        self.wait_clickable(test_data.login.LOGIN_BTN).click()
    def click_logout_btn(self):
        self.wait_clickable(test_data.homepage.LOG_OUT).click()

    def verify_valid_signup_account_info(self):
        self.click_signup_login_menu()
        fake =Faker()
        email_address = f"{fake.first_name()}_emailgrey@example.org"
        password = "Password123!"

        self.type_name_email_signup(fake.name(), email_address)
        self.click_signup_btn()

        self.set_title("mrs")
        self.enter_password(password)

        self.enter_date_of_birth('6','11', '2002')
        self.enter_address_information(fake.name(), fake.name(), fake.company(), fake.address(),
                                       fake.address(), "Canada", fake.state(), fake.city(),
                                       fake.zipcode(), "1231239")

        self.click_create_account()

        current_result_url = self.get_account_created_url("https://automationexercise.com/account_created")
        current_result_account_created = self.get_account_created_message()

        return current_result_url, current_result_account_created.strip(), email_address, password

    def verify_signup_with_existing_email(self):
        self.click_signup_login_menu()
        name = "name"
        email = "123@gmail.com"
        self.type_name_email_signup(name, email)
        self.click_signup_btn()

        current_result_email_exist_message = self.get_email_exist_message()

        return current_result_email_exist_message.strip()

    def verify_signup_without_email_password(self):
        self.click_signup_login_menu()
        self.type_name_email_signup("", "")
        self.click_signup_btn()

        current_result_fill_out_field = self.validation_fillout_this_field(test_data.signup.NAME)

        return current_result_fill_out_field.strip()

    def verify_valid_login(self):
        self.click_signup_login_menu()

        self.type_email_password_login(test_data.email, test_data.password)
        self.click_login_btn()

        current_url = self.get_url("https://automationexercise.com/")

        return current_url

