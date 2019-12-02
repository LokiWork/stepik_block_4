from .pages.main_page import MainPage
from .pages.login_page import LoginPage


def test_guest_can_go_to_login_page(browser):
	link = "http://selenium1py.pythonanywhere.com/"
	page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
	page.open()                      # открываем страницу
	page.go_to_login_page() 

def test_guest_should_see_login_link(browser):
	link = "http://selenium1py.pythonanywhere.com/"
	page = MainPage(browser, link)
	page.open()
	page.should_be_login_link()

def test_open_login_page_and_check_forms(browser):
	link = "http://selenium1py.pythonanywhere.com/"
	page = MainPage(browser, link)
	page.open()
	page.go_to_login_page()
	login_link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
	login_page = LoginPage(browser, login_link)
	login_page.should_be_login_page()
