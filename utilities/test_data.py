from selenium.webdriver.common.by import By

BASE_URL = "https://automationexercise.com/"
email = "testemailautomation123!@gmail.com"
password = "testemailautomation123password"


class homepage:
    SIGNUP_LOGIN_MENU = By.XPATH, "//a[normalize-space()='Signup / Login']"
    PRODUCTS_MENU = By.CSS_SELECTOR, "a[href='/products']"
    CART_MENU = By.XPATH, "//a[normalize-space()='Cart']"
    LOG_OUT = By.XPATH, "//a[normalize-space()='Logout']"
class login:
    SIGNUP_LOGIN_MENU = By.XPATH, "//a[normalize-space()='Signup / Login']"
    EMAIL = By.XPATH, "//input[@data-qa='login-email']"
    PASSWORD = By.XPATH, "//input[@placeholder='Password']"
    LOGIN_BTN = By.XPATH, "//button[normalize-space()='Login']"
class products:
    CONTINUE_SHOPPING = By.XPATH, "(//button[normalize-space()='Continue Shopping'])[1]"
class cart:
    DELETE = By.XPATH, "(//a[@class='cart_quantity_delete'])[1]"
    CART_EMPTY_MESSAGE = By.XPATH, "//b[normalize-space()='Cart is empty!']"
    HERE = By.XPATH, "//u[normalize-space()='here']"
    PROCEED_CHECKOUT_BTN = By.XPATH, "//a[@class='btn btn-default check_out']"
    COMMENT =  By.XPATH, "//textarea[@name='message']"
    PLACE_ORDER = By.XPATH, "//a[@class='btn btn-default check_out']"

    NAME_ON_CARD = By.XPATH, "//input[@name='name_on_card']"
    CARD_NUMBER = By.XPATH, "//input[@name='card_number']"
    CVC = By.XPATH, "//input[@name='cvc']"
    MONTH = By.XPATH, "//input[@name='expiry_month']"
    YEAR = By.XPATH, "//input[@name='expiry_year']"
    PAY_AND_CONFIRM_ORDER = By.XPATH, "//button[@id='submit']"

    ORDER_PLACE_MESSAGE = By.XPATH, "//b[normalize-space()='Order Placed!']"
class signup:
    NAME = By.XPATH, "//input[@name='name']"
    EMAIL_ADDRESS = By.XPATH, "//input[@data-qa='signup-email']"
    SIGNUP_BTN = By.XPATH, "//button[normalize-space()='Signup']"

    EMAIL_ALREADY_EXIST_MESSAGE = By.XPATH, "//p[normalize-space()='Email Address already exist!']"

    MR = By.XPATH, "(//input[@id='id_gender1'])[1]"
    MRS = By.XPATH, "(//input[@id='id_gender2'])[1]"
    PASSWORD = By.XPATH, "//input[@name='password']"
    DAY = By.XPATH, "//select[@name='days']"
    MONTH = By.XPATH, "//select[@name='months']"
    YEAR = By.XPATH, "//select[@name='years']"

    NEWS_LETTER = By.XPATH, "//label[@for='newsletter']"
    SPECIAL_OFFER = By.XPATH, "//label[@for='optin']"

    FIRST_NAME = By.XPATH, "//input[@name='first_name']"
    LAST_NAME = By.XPATH, "//input[@name='last_name']"
    COMPANY = By.XPATH, "//input[@name='company']"

    ADDRESS_ONE = By.XPATH, "(//input[@name='address1'])[1]"
    ADDRESS_TWO = By.XPATH, "(//input[@name='address2'])[1]"
    COUNTRY = By.XPATH, "//select[@name='country']"
    STATE = By.XPATH, "//input[@name='state']"
    CITY = By.XPATH, "//input[@name='city']"
    ZIP_CODE = By.XPATH, "//input[@name='zipcode']"
    MOBILE_NO = By.XPATH, "//input[@name='mobile_number']"
    CREATE_ACCOUNT_BTN = By.XPATH, "//button[normalize-space()='Create Account']"

    ACCOUNT_CREATED_MESSAGE = By.XPATH, "//b[normalize-space()='Account Created!']"
    CONTINUE_BTN = By.XPATH, "(//a[normalize-space()='Continue'])[1]"



