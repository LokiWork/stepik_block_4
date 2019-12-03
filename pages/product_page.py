from .base_page import BasePage
from .locators import Products

class ProductPage(BasePage):

	def guest_can_add_product_to_basket(self):
		self.click_button_add_to_basket()
		self.get_code()
		self.book_name_matched()
		self.book_price_matched()

	def get_book_name(self):
		return self.browser.find_element(*Products.BOOK_TITLE).text

	def get_price(self):
		return self.browser.find_element(*Products.BOOK_PRICE).text

	def click_button_add_to_basket(self):
		self.browser.find_element(*Products.BUTTON_ADD_TO_BASKET).click()

	def book_name_matched(self):
		assert self.browser.find_element(*Products.MESSAGE_BOOK_NAME).text == self.get_book_name(), "Book name is not equals"

	def book_price_matched(self):
		assert self.browser.find_element(*Products.MESSAGE_BOOK_PRICE).text == self.get_price(), "Price is not match"

	def get_code(self):
		self.solve_quiz_and_get_code()

	def block_with_message_is_not_presetn(self):
		assert self.is_not_element_present(*Products.MESSAGES), "The block with message is not present"

	def block_with_message_is_disappeared(self):
		assert self.is_disappeared(*Products.MESSAGES), "The block is not hidden"