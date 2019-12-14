from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):

        assert "login" in self.browser.current_url

    def should_be_login_form(self):

        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not present"

    def should_be_register_form(self):

        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not present"

    def register_new_user(self, email, password):
        login = self.browser.find_element(*LoginPageLocators.LOGIN_NAME)
        login.send_keys(email)
        password_field1 = self.browser.find_element(*LoginPageLocators.LOGIN_PASS1)
        password_field2 = self.browser.find_element(*LoginPageLocators.LOGIN_PASS2)
        password_field1.send_keys(password)
        password_field2.send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()

        self.should_be_authorized_user()
