import random
import string
import time

from faker import Faker

import test_data
from pages.base_page import BasePage


class SignupPage(BasePage):

    def verify_signup_without_name_and_email(self):
        time.sleep(2)

        #click login/singup menu
        self.wait_clickable(test_data.homepage.SIGNUP_LOGIN_MENU, 15).click()

        time.sleep(1)

        #check the page url
        assert self.url_is("https://automationexercise.com/login")

        #click signup btn
        self.wait_clickable(test_data.signup.SIGNUP_BTN, 15).click()
        time.sleep(0.5)

        #asssert validation message
        assert "Please fill out this field." in self.get_validation_message(test_data.signup.NAME, 15)

    def verify_signup_with_existing_account(self):
        time.sleep(2)

        # input name
        namevalue = "www"
        self.send_keys(15, test_data.signup.NAME, namevalue)
        time.sleep(0.5)

        # input email
        emailvalue = "www@gmail.com"
        self.send_keys(15, test_data.signup.EMAIL_ADDRESS, emailvalue)

        time.sleep(0.5)
        # click signup btn
        self.wait_clickable(test_data.signup.SIGNUP_BTN, 15).click()
        time.sleep(0.5)

        assert self.wait_visibility(test_data.signup.EMAIL_ALREADY_EXIST_MESSAGE, 15)

    def verify_signup_with_invalid_email(self):
        time.sleep(2)

        # input name
        namevalue = ''.join(random.choices(string.ascii_lowercase, k=7))
        self.send_keys(15, test_data.signup.NAME, namevalue)

        time.sleep(0.5)

        # input email
        emailvalue = "emailsvalue"
        self.send_keys(15, test_data.signup.EMAIL_ADDRESS, emailvalue)

        time.sleep(0.5)

        # click signup btn
        self.wait_clickable(test_data.signup.SIGNUP_BTN, 15).click()
        time.sleep(0.5)

        assert "Please include an '@' in the email address." in self.get_validation_message(test_data.signup.EMAIL_ADDRESS, 15)

    def verify_signup_with_valid_credentials(self):
        time.sleep(2)

        # input name
        namevalue = ''.join(random.choices(string.ascii_lowercase, k=7))
        self.send_keys(15, test_data.signup.NAME, namevalue)

        time.sleep(0.5)

        # input email
        emailvalue = ''.join(random.choices(string.ascii_lowercase, k=7))
        self.send_keys(15, test_data.signup.EMAIL_ADDRESS, f"{emailvalue}@gmail.com")

        time.sleep(0.5)

        # click signup btn
        self.wait_clickable(test_data.signup.SIGNUP_BTN, 15).click()
        time.sleep(1)

        #click mr
        self.wait_clickable(test_data.signup.MR, 15).click()
        time.sleep(0.5)

        # input password
        self.send_keys(15, test_data.signup.PASSWORD, test_data.PASSWORD)
        time.sleep(0.5)

        #select day
        day = self.wait_clickable(test_data.signup.DAY, 15)
        day.click()
        time.sleep(0.5)
        self.action_click(self.select_by_visible_text(day, "25"))

        time.sleep(0.5)

        # select month
        month = self.wait_clickable(test_data.signup.MONTH, 15)
        month.click()
        time.sleep(0.5)
        self.action_click(self.select_by_visible_text(month, "December"))

        time.sleep(0.5)

        # select year
        year = self.wait_clickable(test_data.signup.YEAR, 15)
        year.click()
        time.sleep(0.5)
        self.action_click(self.select_by_visible_text(year, "1997"))

        time.sleep(0.5)

        #click newsletter
        self.wait_clickable(test_data.signup.NEWS_LETTER, 15).click()

        time.sleep(0.5)

        #click special offers
        self.wait_clickable(test_data.signup.SPECIAL_OFFER, 15).click()

        time.sleep(0.5)
        #scroll down
        self.scroll_by_amount(0, 250)

        fake = Faker()
        #input firstname
        firstnamevalue = fake.first_name()
        self.send_keys(15, test_data.signup.FIRST_NAME, firstnamevalue)
        time.sleep(0.5)

        # input lastname
        lastnamevalue = fake.last_name()
        self.send_keys(15, test_data.signup.LAST_NAME, lastnamevalue)
        time.sleep(0.5)

        # input company
        companyvalue = "company"
        self.send_keys(15, test_data.signup.COMPANY, companyvalue)
        time.sleep(0.5)

        # input address one
        addressonevalue = "address one"
        self.send_keys(15, test_data.signup.ADDRESS_ONE, addressonevalue)
        time.sleep(0.5)

        # input address two
        addresstwovalue = "address two"
        self.send_keys(15, test_data.signup.ADDRESS_TWO, addresstwovalue)
        time.sleep(0.5)

        # select country
        country = self.wait_clickable(test_data.signup.COUNTRY, 15)
        country.click()
        time.sleep(0.5)
        self.action_click(self.select_by_visible_text(country, "Canada"))

        # input state
        statevalue = fake.state()
        self.send_keys(15, test_data.signup.STATE, statevalue)
        time.sleep(0.5)

        # input CITY
        cityvalue = fake.city()
        self.send_keys(15, test_data.signup.CITY, cityvalue)
        time.sleep(0.5)

        # input zip code
        zipcodevalue = "34341"
        self.send_keys(15, test_data.signup.ZIP_CODE, zipcodevalue)
        time.sleep(0.5)

        # input mobile no.
        mobileNovalue = fake.numerify("########")
        self.send_keys(15, test_data.signup.MOBILE_NO, mobileNovalue)
        time.sleep(0.5)

        #click create account btn
        self.wait_clickable(test_data.signup.CREATE_ACCOUNT_BTN, 15).click()

        time.sleep(1)

        #assert page url and title and account created message
        assert self.title_is("Automation Exercise - Account Created")
        assert self.url_is("https://automationexercise.com/account_created")
        assert self.wait_visibility(test_data.signup.ACCOUNT_CREATED_MESSAGE, 15)

        time.sleep(0.5)

        #click continue btn
        self.wait_clickable(test_data.signup.CONTINUE_BTN,15).click()