from .base_page import BasePage
from .locators import MainPageLocators
from selenium.webdriver.common.by import By

class MainPage(BasePage):

	# def __init__(self, *args, **kwargs):
 #        super(MainPage, self).__init__(*args, **kwargs)

	def calculate_response_code(self):
		self.solve_quiz_and_get_code()