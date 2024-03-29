from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
	page = ProductPage(browser, link)
	page.open()
	page.guest_can_add_product_to_basket()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser): 
	link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
	page = ProductPage(browser, link)
	page.open()
	page.click_button_add_to_basket()
	page.block_with_message_is_not_presetn()

def test_guest_cant_see_success_message(browser):
	link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
	page = ProductPage(browser, link)
	page.open()
	page.block_with_message_is_not_presetn()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser): 
	link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
	page = ProductPage(browser, link)
	page.open()
	page.click_button_add_to_basket()
	page.block_with_message_is_disappeared()

def test_guest_should_see_login_link_on_product_page(browser):
	link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
	page = ProductPage(browser, link)
	page.open()
	page.should_be_login_link()

@pytest.mark.xfail
def test_guest_can_go_to_login_page_from_product_page(browser):
	link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
	page = ProductPage(browser, link)
	page.open()
	page.go_to_login_page()



class TestUserAddToBasketFromProductPage():

	@pytest.mark.need_review
	def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
		link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/'
		page = ProductPage(browser, link)
		page.open()
		page.click_on_button_basket()
		basket_page = BasketPage(browser, browser.current_url)
		basket_page.text_basket_is_empty_en()
		basket_page.not_product_in_basket()

	@pytest.mark.need_review
	def test_guest_can_add_product_to_basket(self, browser):
		link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
		page = ProductPage(browser, link)
		page.open()
		page.add_product_to_basket_no_alert()

	@pytest.mark.need_review
	def test_user_cant_see_success_message(self, browser):
		link = "http://selenium1py.pythonanywhere.com/"
		page = ProductPage(browser, link)
		page.open()
		page.go_to_login_page()
		login = LoginPage(browser, browser.current_url)
		login.register_new_user()
		page = ProductPage(browser, link)
		page.should_be_authorized_user()
		page.click_on_button_basket()
		basket_page = BasketPage(browser, browser.current_url)
		basket_page.text_basket_is_empty_en()
		basket_page.not_product_in_basket()

	@pytest.mark.need_review
	def test_user_can_add_product_to_basket(self, browser):
		link = "http://selenium1py.pythonanywhere.com/"
		page = ProductPage(browser, link)
		page.open()
		page.go_to_login_page()
		login = LoginPage(browser, browser.current_url)
		login.register_new_user()
		link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
		page = ProductPage(browser, link)
		page.open()
		page.add_product_to_basket_no_alert()