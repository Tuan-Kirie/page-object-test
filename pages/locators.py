from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    GO_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".basket-mini > .btn-group > a")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_EMAIL = (By.CSS_SELECTOR, 'input[name="login-username"]')
    LOGIN_PASSWORD = (By.CSS_SELECTOR, 'input[name="login-password"]')
    LOGIN_SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[name="login_submit"]')
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, 'input[name="registration-email"]')
    REGISTRATION_PASSWORD_FIRST = (By.CSS_SELECTOR, 'input[name="registration-password1"]')
    REGISTRATION_PASSWORD_SECOND = (By.CSS_SELECTOR, 'input[name="registration-password2"]')
    REGISTRATION_SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[name="registration_submit"]')


class ProductPageLocators:
    PRODUCT_PAGE_ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_PAGE_PRICE = (By.CSS_SELECTOR, '.product_main > .price_color')
    PRODUCT_PAGE_NAME = (By.CSS_SELECTOR, 'h1')
    PRODUCT_PAGE_BASKET_TOTAL_PRICE = (By.CSS_SELECTOR, '#messages > .alert:nth-child(3) > .alertinner > p > strong')
    PRODUCT_PAGE_BASKET_NAME_OF_PRODUCT = (By.CSS_SELECTOR, '#messages > .alert:nth-child(1) > .alertinner > strong')
    PRODUCT_PAGE_SUCCEED_MESSAGE = (By.CSS_SELECTOR, "div.alertinner")


class BasketPageLocators:
    BASKET_PAGE_ITEM = (By.CSS_SELECTOR, ".basket-items")
