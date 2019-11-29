
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='pl',
                     help="Choose language:")

@pytest.fixture(scope="function")
def browser(request):
	language = request.config.getoption("language")
	print("\nstart browser for test..")
	options = Options()
	if language is None:
		print("Set Poland language..")
		options.add_experimental_option('prefs', {'intl.accept_languages':'pl' })
	else:
		print("Set language is {} ..".format(language))
		options.add_experimental_option('prefs',{'intl.accept_languages':language})
	browser = webdriver.Chrome(options=options)
	yield browser
	print("\nquit browser..")
	browser.quit()