from .base_page import BasePage
from .locators import LoginPageLocators, BasePageLocators
from faker import Faker

class LoginPage(BasePage):

    def register_new_user(self):
        f = Faker()
        password = f.password()
        self.browser.find_element(*LoginPageLocators.INPUT_REGISTRATION_EMAIL).send_keys(f.email())
        self.browser.find_element(*LoginPageLocators.INPUT_REGISTRATION_PASS).send_keys(password)
        self.browser.find_element(*LoginPageLocators.INPUT_REGISTRATION_PASS_REP ).send_keys(password)
        self.browser.find_element(*LoginPageLocators.BUTTON_REGISTRATION).click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        url = self.browser.current_url
        assert 'login' in url, "word \"login\" not in url"

    def should_be_login_form(self):
        assert self.browser.find_element(*LoginPageLocators.LOGIN_FORM).is_displayed(), "Login form not displayed"

    def should_be_register_form(self):
        assert self.browser.find_element(*LoginPageLocators.REGISTRATION_FORM).is_displayed(), "Registration form not displayed"
