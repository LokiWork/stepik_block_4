from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException


class MainPageLocators():
    # LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    pass

class BasePageLocators():
	LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
	LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class LoginPageLocators():
	LOGIN_FORM = (By.ID, 'login_form')
	INPUT_AUTH_LOGIN = (By.ID, "id_login-username")
	INPUT_AUTH_PASS = (By.ID, "id_login-password")
	LINK_FORGOT_PASS = (By.XPATH, "//form[@id='login_form']//a[contains(@href, 'password-reset')]")
	BUTTON_LOGIN = (By.NAME, 'login_submit')

	REGISTRATION_FORM = (By.ID, 'register_form')
	INPUT_REGISTRATION_EMAIL = (By.ID, 'id_registration-email')
	INPUT_REGISTRATION_PASS = (By.ID, 'id_registration-password1')
	INPUT_REGISTRATION_PASS_REP = (By.ID, 'id_registration-password2')
	BUTTON_REGISTRATION = (By.NAME, 'registration_submit')

class Products():
	BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, '.btn.btn-lg.btn-primary.btn-add-to-basket')
	BOOK_TITLE = (By.XPATH, "//div[@id='content_inner']//h1")
	BOOK_PRICE = (By.XPATH, "//p[@class='price_color']")
	MESSAGES = (By.XPATH, "//div[@id='messages']/div[1]")
	MESSAGE_BOOK_NAME = (By.XPATH, "//div[@id='messages']//div[1]/div/strong")
	MESSAGE_BOOK_PRICE = (By.XPATH, "//div[@id='messages']//div[3]//strong")