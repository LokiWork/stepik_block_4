from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


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