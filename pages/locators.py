from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    LOGIN_NAME = (By.CSS_SELECTOR,"#id_registration-email")
    LOGIN_PASS1 = (By.CSS_SELECTOR, "#id_registration-password1")
    LOGIN_PASS2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form button")

class ProductPageLocators():
    BUTTON_ADD_TO_CARD = (By.CSS_SELECTOR, ".btn-add-to-basket")
    MESSAGE_BOX = (By.ID, "messages")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    MESSAGES = (By.CSS_SELECTOR, ".alertinner strong")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET_EMPTY_TEXT = (By.CSS_SELECTOR, "#content_inner>p")
    BASKET_ITEMS_BOX = (By.CSS_SELECTOR, ".basket-items")
