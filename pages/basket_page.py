from .base_page import BasePage
from .locators import Basket


class BasketPage(BasePage):

	def text_basket_is_empty_en(self):
		assert 'Your basket is empty.' in self.browser.find_element(*Basket.EMPTY_BASKET_TEXT).text, "Text /'Your basket is empty.'/is not presetn on page"

	def not_product_in_basket(self):
		assert self.is_disappeared(*Basket.PRODUCT_ITEMS)	